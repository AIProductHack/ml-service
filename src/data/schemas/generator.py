import os
import json
from typing import Any

import dotenv

from pydantic import BaseModel
from models import (
    Alert,
    Button,
    Box,
    Card,
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
    Sidebar,
    Typography,
]


class ComponentSchemaGenerator:
    @classmethod
    def generate_schema(cls, component: type[BaseModel]) -> dict[str, Any]:
        return component.model_json_schema(mode="serialization")


if __name__ == "__main__":
    for component in COMPONENTS:
        schema = ComponentSchemaGenerator.generate_schema(component)
        with open(COMPONENT_SCHEMA_EXAMPLE_PATH + schema["title"] + ".json", "w") as f:
            json.dump(schema, f, indent=4, ensure_ascii=False)
