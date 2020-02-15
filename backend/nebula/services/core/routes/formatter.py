from typing import List
from io import BytesIO

from fastapi import Depends, File, Header, UploadFile
from openpyxl import load_workbook

from services.api import responses
from formatter import format_excel
from . import api


def load_values_as_array(file: BytesIO) -> List:
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


@api.post('/format_excel', responses=responses)
def format_excel_to_yml(id: int, file: UploadFile = File(...)):
    elements = load_values_as_array(BytesIO(file.file.read()))
    # TODO, FIXME: get instruction from mongo by id

    return format_excel(elements, [])
