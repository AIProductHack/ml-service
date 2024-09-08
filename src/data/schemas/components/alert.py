from typing import Literal
from pydantic import BaseModel

SEVERITY_VARIANTS = Literal[
    "success",
    "error",
    "warning",
    "info",
]


class Alert(BaseModel):
    title: str | None = None
    severity: SEVERITY_VARIANTS = "success"
    className: str | None = None
    content: str | None = None
