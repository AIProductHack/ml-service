import json
from typing import Annotated
from fastapi import APIRouter, File
from .schemas import GenerationResponse
from generators import (
    GeneratorType,
    GeneratorFactory,
)

router = APIRouter(prefix="/generation", tags=["generation"])


@router.post("/from_text", status_code=200, response_model=GenerationResponse)
def generate_from_text(
    text: str,
    generator_type: GeneratorType = GeneratorType.CHATGPT
):
    model = GeneratorFactory.get_generator(generator_type.value)
    try:
        response = model.call_api(text)
    except Exception as e:
        print(e)
        model.refresh_token()
    finally:
        response = model.call_api(text)
    print(response)
    try:
        components = response[0]
        css = response[1]
        return GenerationResponse(data=components, css=css)
    except:
        return GenerationResponse()


@router.post("/from_audio", status_code=200, response_model=GenerationResponse)
def generate_from_audio(file: Annotated[bytes, File()]):
    return {200: "ok"}


@router.post("/from_image", status_code=200, response_model=GenerationResponse)
def generate_from_image(file: Annotated[bytes, File()]):
    return {200: "ok"}
