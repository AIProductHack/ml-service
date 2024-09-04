from typing import Literal
from pydantic import BaseModel


TYPOGRAPHY_VARIANTS = Literal[
    'Heading1',
    'Heading2',
    'Heading3',
    'Heading4',
    'Subheading1',
    'Subheading2',
    'Subheading2-Medium',
    'Subheading3',
    'Subheading3-Medium',
    'Body',
    'Body-Medium',
    'Body-Bold',
    'Body1',
    'Body1-Medium',
    'Body1Table-Medium',
    'Body1Mono-Medium',
    'Body1Mono-Bold',
    'Body1-Bold',
    'Body2',
    'Body2-Medium',
    'Body2Mono-Medium',
    'Body2Mono-Bold',
    'Body2-Bold',
    'Caption',
    'Caption-Medium',
    'Caption-Bold',
    'CaptionMono',
    'CaptionMono-Medium',
    'CaptionMono-Bold',
    'Additional-Bold'
]


class Typography(BaseModel):
    variant: TYPOGRAPHY_VARIANTS | None = None
    color: str | None = None
    className: str | None = None
    children: list[object] = list()
    content: str | None = None
