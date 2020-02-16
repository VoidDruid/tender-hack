from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    ok: bool = False
    error: Union[str, Dict, List] = 'Unknown error'


class CorrectResponse(BaseModel):
    ok: bool = True
    info: Optional[Union[str, Dict, List]] = None


class ORMModel(BaseModel):  # inherit all models from this one
    class Config:
        orm_mode = True
