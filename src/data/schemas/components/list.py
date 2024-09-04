from pydantic import BaseModel


class List(BaseModel):
    children: list[object] = []
    className: str | None = None
