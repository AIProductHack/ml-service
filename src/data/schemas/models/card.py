import enum
from pydantic import BaseModel
from data.schemas.enums import SizeMapping


class OrientationMapping(str, enum.Enum):
    vertical = 'vertical'
    horizontal = 'horizontal'


class IndicatorStatusMapping(str, enum.Enum):
    default = 'default'
    success = 'success'
    error = 'error'
    warning = 'warning'
    info = 'info'


class Card(BaseModel):
    orientation: OrientationMapping = OrientationMapping.vertical
    indicatorSize: SizeMapping = SizeMapping.s
    indicatorStatus: IndicatorStatusMapping = IndicatorStatusMapping.default
    className: str | None = None
    children: list[object] = list()