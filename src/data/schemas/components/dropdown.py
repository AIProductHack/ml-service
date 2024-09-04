from pydantic import BaseModel
from .button import ButtonSize


class Dropdown(BaseModel):
    disabled: bool | None = None
    className: str | None = None
    size: ButtonSize = ButtonSize.m
    children: list[object]
    buttonChildren: list[object]
