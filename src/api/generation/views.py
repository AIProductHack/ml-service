from typing import Annotated
from fastapi import APIRouter, File
from .schemas import GenerationResponse

router = APIRouter(prefix="/generation", tags=["generation"])


@router.post("/from_text", status_code=200, response_model=GenerationResponse)
def generate_from_text(text: str):
    return {200: "ok"}


@router.post("/from_audio", status_code=200, response_model=GenerationResponse)
def generate_from_audio(file: Annotated[bytes, File()]):
    return {200: "ok"}


@router.post("/from_image", status_code=200, response_model=GenerationResponse)
def generate_from_image(file: Annotated[bytes, File()]):
    return {200: "ok"}
