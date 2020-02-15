from typing import List, Dict
from io import BytesIO

from fastapi import Depends, File, Header, UploadFile
from openpyxl import load_workbook

from services.api import responses, OK
from formatter import format_excel
from . import api
from services.dependencies import get_db
from pymongo.database import Database

def load_values_as_array(file) -> List:
    elements = []
    wb = load_workbook(filename=file)
    active_sheet = wb.active
    max_row = active_sheet.max_row
    max_col = active_sheet.max_column

    for r in range(1, max_row + 1):
        element = []
        for c in range(1, max_col + 1):
            element.append(active_sheet.cell(row=r, column=c).value)
        for i in element:
            if i is not None:
                elements.append(element)
                break
    return elements

test_instruction = [
    None,
    None,
    None,
    None,
    {
        "name": "products",
        "type": "array",
        "fields": [
            {
                "name": "number",
                "index": 0
            },
            {
                "name": "code",
                "index": 1
            },
            {
                "name": "name",
                "index": 1
            }
        ]
    }
]


@api.post('/format_excel', responses=responses)
def format_excel_to_yml(id: int, file: UploadFile = File(...)):
    elements = load_values_as_array(BytesIO(file.file.read()))

    instructions = test_instruction  # TODO, FIXME: get instruction from mongo by id

    return format_excel(elements, instructions)


@api.post('/instructions', responses=responses)
def save_instructions(id: int, instructions: List, db: Database = Depends(get_db)):
    db.insert_one({"user_id": str(id), "instructions": instructions})
    print(instructions)
    return OK(None)
