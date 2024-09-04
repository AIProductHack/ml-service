import os
import json
from typing import Any

import dotenv

from pydantic import BaseModel
from components import (
    Alert,
    Box,
    Button,
    Card,
    Checkbox,
    Dropdown,
    List,
    Scrollbar,
    Sidebar,
    Typography,
)

dotenv.load_dotenv()

COMPONENT_SCHEMA_EXAMPLE_PATH = os.getenv("COMPONENT_SCHEMA_EXAMPLE_PATH")

COMPONENTS = [
    Alert,
    Button,
    Box,
    Card,
    Checkbox,
    Dropdown,
    List,
    Scrollbar,
    Sidebar,
    Typography,
]


class ComponentDataDirector:
    @classmethod
    def generate_schema(cls, component: type[BaseModel]) -> dict[str, Any]:
        return component.model_json_schema(mode="serialization")

    @classmethod
    def create_dumped_instance(cls, component: type[BaseModel], data: dict[str, Any]) -> dict[str, Any]:
        return component(**data).model_dump(exclude_unset=True)


if __name__ == "__main__":
    for component in COMPONENTS:
        schema = ComponentDataDirector.generate_schema(component)
        with open(COMPONENT_SCHEMA_EXAMPLE_PATH + schema["title"] + ".json", "w") as f:
            json.dump(schema, f, indent=4, ensure_ascii=False)
