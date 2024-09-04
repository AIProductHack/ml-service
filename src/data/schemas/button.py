import json
import enum
from pydantic import BaseModel


class ButtonVariant(str, enum.Enum):
    primary = 'primary'
    secondary = 'secondary'
    grey = 'grey'
    black = 'black'
    success = 'success'
    warning = 'warning'
    error = 'error'
    info = 'info'


class ButtonSize(str, enum.Enum):
    m = 'm'
    s = 's'
    xs = 'xs'


class ButtonFill(str, enum.Enum):
    solid = 'solid'
    outline = 'outline'
    clear = 'clear'


class ButtonNodesPosition(str, enum.Enum):
    left = 'left'
    right = 'right'


class Button(BaseModel):
    variant: ButtonVariant = ButtonVariant.primary
    size: ButtonSize = ButtonSize.m
    fill: ButtonFill = ButtonFill.solid
    content: str | None = None


if __name__ == "__main__":
    print(
        json.dumps(
            Button.model_json_schema(mode="serialization"),
            indent=4,
        )
    )
