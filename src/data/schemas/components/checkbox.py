import enum
from pydantic import BaseModel


class CheckboxColor(str, enum.Enum):
    default = 'default'
    error = 'error'


class Checkbox(BaseModel):
    label: str | None = None
    checked: bool = False
    disabled: bool = False
    color: CheckboxColor = CheckboxColor.default
    multiple: bool = False
    value: str | None = None
    className: str | None = None
