import io
from pprint import pprint
from typing import List

from lxml import etree
from starlette.responses import StreamingResponse

mandatory = {
    'id': None,
    'currencyId': 643,
    'name': None,
    'picture': None,
    'categoryId': None,
    'beginDate': '3 November 1971',
    'endDate': '19 January 2038',
    'price': None,
    'model': None,
    'vendor': 'company',
    'vat': '20',
    'delivery': False,
}

nullable = [
    'NULL',
    'NONE',
    'NAN',
]


def get_header():
    return """
<yml_catalog date="2019-11-01 17:22">
"""


def get_shop():
    return """ 
    <shop>
        <name>BestSeller</name>
        <company>Tne Best inc.</company>
        <url>http://best.seller.ru</url>
        <currencies>
            <currency id="RUR" rate="1"/>
            <currency id="USD" rate="60"/>
        </currencies>
        <categories>
            <category id="1">Бытовая техника</category>
            <category id="10" parentId="1">Мелкая техника для кухни</category>
        </categories>
        <delivery-options>
            <option cost="200" days="1"/>
        </delivery-options>
"""


def offer_transformer(offers: List):
    res = ''
    k = None
    for key in offers:
        k = key
        break

    for offer in offers[k]:
        for man in mandatory:
            if offer.get(man, None) is None:
                offer[man] = {'value': '🤔'}

        root = etree.Element('offer', id=str(offer.get('id')['value']))

        dimen = offer.get('dimensions', None)

        if dimen:
            for i in nullable:
                if i in dimen['value']:
                    offer['dimensions']['value'] = dimen['value'].replace(i, '0')

        params = []
        for key, value in offer.items():
            if key == 'id':
                continue
            is_param = value.get('is_param', False)
            if is_param:
                if value['value'] not in nullable:
                    params.append((key, value['value']))
            else:
                if key in mandatory and (
                    value['value'] in nullable or value['value'] == '🤔' or value['value'] is None
                ):
                    child = etree.SubElement(root, key)
                    default = mandatory[key]
                    child.text = str(default) if default is not None else '🤔'
                elif key not in mandatory and value['value'] not in nullable:
                    child = etree.SubElement(root, key)
                    child.text = str(value['value'])
                elif key in mandatory:
                    child = etree.SubElement(root, key)
                    child.text = str(value['value'])

        for param in params:
            child = etree.SubElement(root, 'param', name=param[0])
            child.text = str(param[1])
        res = res + etree.tostring(root, encoding='utf-8', pretty_print=True).decode()

    res = get_header() + get_shop() + '\n' + res + '\n</shop>\n</yml_catalog>'
    return StreamingResponse(io.BytesIO(res.encode('utf-8')), media_type='text/xml')
