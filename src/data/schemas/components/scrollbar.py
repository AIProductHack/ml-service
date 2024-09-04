import enum
from pydantic import BaseModel


class Overflow(str, enum.Enum):
    visible = 'visible'
    hidden = 'hidden'
    scroll = 'scroll'
    auto = 'auto'


class Scrollbar(BaseModel):
    children: list[object]
    className: str | None = None
    overflowX: Overflow | None = None
    overflowY: Overflow | None = None
    overflow: Overflow | None = None
