import json
import enum
from pydantic import BaseModel
from default import SizeMapping


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


if __name__ == "__main__":
    print(
        json.dumps(
            Card.model_json_schema(mode="serialization"),
            indent=4,
        )
    )
