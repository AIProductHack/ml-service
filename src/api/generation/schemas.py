from typing import TypeAlias, Union
from pydantic import BaseModel
from src.data.schemas.components import (
    Alert,
    Button,
    Box,
    Card,
    Checkbox,
    Dropdown,
    List,
    Sidebar,
    Scrollbar,
    Typography,
)

Components: TypeAlias = Union[
    Alert,
    Button,
    Box,
    Card,
    Checkbox,
    Dropdown,
    List,
    Sidebar,
    Scrollbar,
    Typography,
]


class GenerationResponse(BaseModel):
    data: list[Components] = []
