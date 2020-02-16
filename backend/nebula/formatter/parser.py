from collections import defaultdict
from copy import deepcopy
from pprint import pprint

from conf import DEBUG

from .transformer import offer_transformer

_print = print


def print(*args):  # noqa
    return
    if not DEBUG:
        return
    for obj in args:
        if isinstance(obj, str):
            _print(obj)
        else:
            pprint(obj)
    _print()


def to_iterator(array):
    yield from array


def getter(attribute: str):
    return lambda obj: obj.get(attribute)


FILLED_TRANSFERED_FLAG = '_is_filled_transfered'
OUTPUT_FIELD_KEYS = '_outputs'
TO_REMOVE = '_to_remove'
IS_COLLECTING_MULTIPLES = '_is_collecting_mult'
SYSTEM_FIELDS = [FILLED_TRANSFERED_FLAG, OUTPUT_FIELD_KEYS, TO_REMOVE, IS_COLLECTING_MULTIPLES]
TRANSFERED_FIELDS = [
    'is_param',
]


(
    get_fields,
    get_name,
    get_type,
    get_index,
    get_is_multiple,
    get_is_optional,
    get_output,
    get_to_remove,
    get_output_keys,
    get_is_collecting_multiples,
    get_parent_of,
) = [
    getter(attr)
    for attr in [
        'fields',
        'name',
        'type',
        'index',
        'is_multiple',
        'is_optional',
        'output',
        TO_REMOVE,
        OUTPUT_FIELD_KEYS,
        IS_COLLECTING_MULTIPLES,
        'parent_of',
    ]
]


def multiples_satisfied(row, schema):
    for field in get_fields(schema):
        if get_is_multiple(field) and not row[get_index(field)]:
            return False
    return True


def create_check_function(schema):
    def check(row, parsing_context):
        if not schema:
            return False

        fields = get_fields(schema)
        if get_is_collecting_multiples(parsing_context) and multiples_satisfied(row, schema):
            return True

        for field in fields:
            if not get_is_optional(field) and row[get_index(field)] is None:
                return False

        return True

    return check


def next_entitiy_schema(entity_schemas):
    schema = next(entity_schemas)
    check_function = create_check_function(schema)
    return schema, check_function


def clear_specified_fields(object, fields_list):
    for system_field in fields_list:
        object.pop(system_field, None)


def build_output_field(params):
    values = params.pop('values')
    method = params.pop('method')

    if not method:
        value = str(values)
    if method.endswith('join'):
        join_around = method.split('-')[0]
        value = join_around.join([str(value) for value in values])
    if method == 'concat':
        value = ''.join([str(value) for value in values])

    result = params.copy()
    result['value'] = value
    return result


def extract(parsing_context, schema):
    if not parsing_context or not schema:
        return None

    entity = deepcopy(parsing_context)

    outputs = get_output_keys(entity)
    if outputs:
        for field_name, params in outputs.items():
            entity[field_name] = build_output_field(params)

    for field in get_fields(schema):
        if not get_is_multiple(field):
            continue
        parent_of = get_parent_of(field)
        if not parent_of:
            continue
        field_name = get_name(field)
        for attribute_name, attribute_value in zip(
            entity[field_name]['value'], entity[parent_of]['value']
        ):
            entity[attribute_name] = {'value': attribute_value, 'is_param': True}

    clear_specified_fields(entity, get_to_remove(entity) or [])
    clear_specified_fields(entity, SYSTEM_FIELDS)
    for field_key in entity:
        clear_specified_fields(entity[field_key], SYSTEM_FIELDS)

    return entity


def fill_transfered_fields(rendered_field, field):
    if rendered_field.get(FILLED_TRANSFERED_FLAG, False):
        return
    rendered_field[FILLED_TRANSFERED_FLAG] = True
    for field_name in TRANSFERED_FIELDS:
        if field_name in field:
            rendered_field[field_name] = field[field_name]


def mark_field_to_remove(parsing_context, field):
    field_name = get_name(field)
    if TO_REMOVE in parsing_context and field_name not in get_to_remove(parsing_context):
        parsing_context[TO_REMOVE].append(get_name(field))
    else:
        parsing_context[TO_REMOVE] = [get_name(field)]


def set_outputs(parsing_context, field, value):
    output = get_output(field)
    if not output:
        return
    if OUTPUT_FIELD_KEYS not in parsing_context:
        parsing_context[OUTPUT_FIELD_KEYS] = {}

    to = output['to']
    method = output.get('method')
    if to in parsing_context[OUTPUT_FIELD_KEYS]:
        parsing_context[OUTPUT_FIELD_KEYS][to]['values'].append(value)
    else:
        parsing_context[OUTPUT_FIELD_KEYS][to] = {'values': [value], 'method': method}

    fill_transfered_fields(parsing_context[OUTPUT_FIELD_KEYS][to], field)
    mark_field_to_remove(parsing_context, field)


def process_row(row: list, schema: dict, parsing_context: dict):
    if not schema:
        return None

    entity = None

    for field in get_fields(schema):
        index = get_index(field)
        is_multiple = get_is_multiple(field)
        if not is_multiple and row[index] is not None:
            should_extract = True
            break
    else:
        should_extract = False

    print(f'{should_extract=}')

    if should_extract:
        entity = extract(parsing_context, schema)
        parsing_context.clear()

    for field in get_fields(schema):
        index = get_index(field)
        name = get_name(field)
        value = row[index]
        is_multiple = get_is_multiple(field)

        if not is_multiple:
            if name not in parsing_context:
                parsing_context[name] = {'value': value}
        else:
            parsing_context[IS_COLLECTING_MULTIPLES] = True
            mark_field_to_remove(parsing_context, field)
            if name in parsing_context:
                parsing_context[name]['value'].append(value)
            else:
                parsing_context[name] = {'value': [value]}

        set_outputs(parsing_context, field, value)
        fill_transfered_fields(parsing_context[name], field)

    return entity


def parse_entities(matrix, instructions):
    entities = defaultdict(list)
    
    try:
        entity_schemas = to_iterator(instructions)
        current_schema, check_match = next_entitiy_schema(entity_schemas)
        parsing_context = {}

        def add(schema, new_entity):
            if new_entity is not None:
                entities[get_name(schema)].append(new_entity)

        for row in matrix:
            print('CURRENT SCHEMA: ', current_schema)
            print('PARSING CONTEXT: ', parsing_context)

            if not check_match(row, parsing_context):
                print('SCHEMA MISMATCH')
                last_schema = current_schema
                add(current_schema, extract(parsing_context, last_schema))
                parsing_context.clear()
                try:
                    current_schema, check_match = next_entitiy_schema(entity_schemas)
                except StopIteration:
                    break
                if not last_schema:
                    print('SKIPPING EMPTY SCHEMA')
                    continue

            add(current_schema, process_row(row, current_schema, parsing_context))

        print('CURRENT SCHEMA: ', current_schema)
        print('PARSING CONTEXT: ', parsing_context)

        add(current_schema, extract(parsing_context, current_schema))
    except Exception:
        pass

    return entities


def format_excel(matrix, instructions):
    if len(instructions) == 0:
        return None

    entities = parse_entities(matrix, instructions)
    print(entities)

    return offer_transformer(entities)
