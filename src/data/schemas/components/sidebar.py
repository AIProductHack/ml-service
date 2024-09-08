import enum
from pydantic import BaseModel


class SidebarVariantMapping(str, enum.Enum):
    default = 'default'
    burger = 'burger'


class SidebarOrientationMapping(str, enum.Enum):
    vertical = 'vertical'
    horizontal = 'horizontal'


class SidebarPositionMapping(str, enum.Enum):
    top = 'top'
    bottom = 'bottom'


class Sidebar(BaseModel):
    variant: SidebarVariantMapping = SidebarVariantMapping.default
    orientation: SidebarOrientationMapping = SidebarOrientationMapping.vertical
    allowFavorites: bool = False
    isLoggedIn: bool | None = None
    systemName: str | None = None
    userName: str | None = None
    userSurname: str | None = None
    children: list[object] = list()
