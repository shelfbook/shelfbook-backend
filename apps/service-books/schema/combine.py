from typing import List

from pydantic import BaseModel
from .book import BookSchema


class BookCombinerSchema(BaseModel):
    ids = List[int]
    book: BookSchema
