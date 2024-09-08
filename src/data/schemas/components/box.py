from pydantic import BaseModel


class Box(BaseModel):
    children: list[object] = list()
    p: str | float | None = None
    px: str | float | None = None
    py: str | float | None = None
    pt: str | float | None = None
    pb: str | float | None = None
    pl: str | float | None = None
    pr: str | float | None = None
    background: str | None = None
    height: str | float | None = None
    width: str | float | None = None
    maxWidth: str | float | None = None
    border: str | None = None
    color: str | None = None
    borderRadius: str | float | None = None
    className: str | None = None
    gap: str | float | None = None
