from typing import List
from lxml import etree
from pprint import pprint
mandatory = ['id', 'currencyId', 'name', 'picture', 'categoryId', 'beginDate', 'endDate', 'price', 'model', 'vendor', 'vat', 'delivery']

elements = [{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1387181},
'name': {'value': 'МОНТАЖ, УСТАНОВКА, СБОРКА ПРОЧЕГО '
'ОБОРУДОВАНИЯ'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'оборудования'},
'Вид товаров': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'прочего оборудования'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1394368},
'name': {'value': 'Бумага для офисной техники '
'SvetoCopy'},
'vendor': {'value': 'SVETOCOPY'},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Бумага для офисной '
'техники'},
'Вид товаров': {'is_param': True,
'value': 'Бумага форматная для '
'офисной техники'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 18122616},
'name': {'value': 'Монтаж, установка, сборка прочего '
'оборудования'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'оборудования'},
'Вид товаров': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'прочего оборудования'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 20917060},
'name': {'value': 'Доставка товаров'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1408900},
'name': {'value': 'Доставка'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 17997218},
'name': {'value': 'Заправка картриджей'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'техники и электроники, за '
'исключением '
'электронно-вычислительных '
'машин, вычислительных '
'сетей и периферийных '
'устройств'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание '
'оргтехники для офиса'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value':

'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1397479},
'name': {'value': 'Уборка'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Услуги по санитарному '
'содержанию, вывозу '
'отходов, уборке'},
'Вид товаров': {'is_param': True,
'value': 'Услуги по уборке зданий и '
'территорий, за исключением '
'крыш, помещений медицинских '
'организаций и помещений '
'образовательных '
'организаций'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 19132083},
'name': {'value': 'Техническое обслуживание'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт прочего '
'оборудования и инвентаря'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1449709},
'name': {'value': 'Изготовление мебели'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Работы по изготовлению, '
'производству'},
'Вид товаров': {'is_param': True,
'value': 'Изготовление мебели'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 19735217},
'name': {'value': 'Разработка проекта'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Разработка проектов'},
'Вид товаров': {'is_param': True,
'value': 'Предпроектные работы'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1278788},
'name': {'value': 'Изготовление макета'},
'vendor': {'value': 'Неизвестен 2'},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Изготовление '
'полиграфической и '
'печатной продукции'},
'Вид товаров': {'is_param': True,
'value': 'Изготовление макетов'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 16622985},
'name': {'value': 'Доставка товара'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value':

'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 16239082},
'name': {'value': 'Техническое обслуживание '
'видеонаблюдения'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт систем '
'видеонаблюдения'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1325384},
'name': {'value': 'Внутригородская перевозка '
'(доставка) грузов'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1413182},
'name': {'value': 'Монтаж, установка, сборка '
'оборудования'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'оборудования'},
'Вид товаров': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'прочего оборудования'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 1291849},
'name': {'value': 'Услуги пультовой охраны, '
'мониторинг систем охранной и '
'аварийной сигнализации'},
'vendor': {'value': 'Неизвестен 2'},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Технические охранные, '
'противопожарные услуги '
'(мероприятия)'},
'Вид товаров': {'is_param': True,
'value': 'Услуги пультовой охраны, '
'мониторинг систем охранной '
'и аварийной сигнализации'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 19358682},
'name': {'value': 'Техническое обслуживание тревожной '
'сигнализации'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт охранного '
'оборудования'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 18324683},
'name': {'value': 'Техническое обслуживание АПС'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт '
'охранно-пожарных систем'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}},
{'dimensions': {'value': 'NULLxNULLxNULL'},
'expiry': {'value': 'NULL'},
'id': {'value': 20357598},
'name': {'value': 'Предварительный медицинский '
'осмотр'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Медицинские осмотры'},
'Вид товаров': {'is_param': True,
'value': 'Медицинские '
'освидетельствования'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'}}]


def offer_transformer(offers: List):
    for offer in offers:
        for man in mandatory:
            if offer.get(man, None) is None:
                offer[man] = {'value': '🤔'}

        root = etree.Element("offer", id=str(offer.get('id')['value']))

        params = []
        for key, value in offer.items():
            if key == 'id':
                continue
            is_param = value.get('is_param', False)
            if is_param:
                if value['value'] != 'NULL':
                    params.append((key, value['value']))
            else:
                if key in mandatory and (value['value'] == 'NULL' or value['value'] == '🤔' or value['value'] is None):
                    child = etree.SubElement(root, key)
                    child.text = '🤔'
                elif key not in mandatory and value['value'] != 'NULL':
                    child = etree.SubElement(root, key)
                    child.text = str(value['value'])
                elif key in mandatory:
                    child = etree.SubElement(root, key)
                    child.text = str(value['value'])

        for param in params:
            child = etree.SubElement(root, "param", name=param[0])
            child.text = str(param[1])
        print(etree.tostring(root, encoding='utf-8', pretty_print=True).decode())

offer_transformer(elements)

