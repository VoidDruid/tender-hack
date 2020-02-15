from collections import defaultdict
from pprint import pprint

from conf import DEBUG

_print = print


def print(*args):  # noqa
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


get_fields, get_name, get_type, get_index, get_is_multiple = [getter(attr) for attr in [
    'fields',
    'name',
    'type',
    'index',
    'is_multiple'
]]


def create_check_function(entity_schema):
    def check(row, parsing_context):
        for field in get_fields(entity_schema):
            if row[get_index(field)] is None:
                return False
        return True
    return check


def next_entitiy_schema(entity_schemas):
    schema = next(entity_schemas)
    check_function = create_check_function(schema)
    return schema, check_function


def extract(parsing_context, schema):
    if not parsing_context or not schema:
        return None
    # TODO: support multiple extraction
    return parsing_context.copy()  # TODO


def process_row(row: list, schema: dict, parsing_context: dict):
    # Если заполнено любое из не is_multiple полей - extract
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
            parsing_context[name] = value
        else:
            if name in parsing_context:
                parsing_context[name].append(value)
            else:
                parsing_context[name] = [value]

    return entity


def parse_entities(matrix, instructions):
    entities = defaultdict(list)

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
            try:
                add(current_schema, extract(parsing_context, current_schema))
                current_schema, check_match = next_entitiy_schema(entity_schemas)
                parsing_context.clear()
            except StopIteration:
                break

        add(current_schema, process_row(row, current_schema, parsing_context))

    print('CURRENT SCHEMA: ', current_schema)
    print('PARSING CONTEXT: ', parsing_context)

    add(current_schema, extract(parsing_context, current_schema))

    return entities


def format_excel(matrix, instructions):
    if len(instructions) == 0:
        return None  # what to return?
    
    entities = parse_entities(matrix, instructions)    
    print(entities)

    return None  # return file
