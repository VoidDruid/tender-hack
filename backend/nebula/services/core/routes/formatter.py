from . import api
from fastapi import Depends, File, Header, UploadFile
from services.api import responses
from openpyxl import load_workbook
from io import BytesIO
from typing import List

g_instructions = [
    {
        "name": "products",
        "type": "array",
        "fields": [
            {
                "name": "name",
                "index": 0
            },
            {
                "name": "description",
                "index": 1
            }
        ]
    },
    {
        "name": "price",
        "type": "single",
        "eval": "float(row[1])"
    }
]


def load_values_as_array(file) -> List:
    elements = []
    wb = load_workbook(filename=file)
    active_sheet = wb.active
    max_row = active_sheet.max_row
    max_col = active_sheet.max_column

    for r in range(2, max_row + 1):
        element = []
        for c in range(1, max_col + 1):
            element.append(active_sheet.cell(row=r, column=c).value)
        for i in element:
            if i is not None:
                elements.append(element)
                break
    return elements


@api.get('/formatter', response_model=responses)
def events_list(id: int, file: UploadFile = File(...)):
    # get instructions from DB by ID
    instructions = g_instructions

    elements = load_values_as_array(BytesIO(file.file.read()))
    return elements


elements =  load_values_as_array('test.xlsx')
print(len(elements), elements)