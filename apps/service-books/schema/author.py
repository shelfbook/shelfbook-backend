from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from schema import BookSchema


class AuthorInSchema(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    birth_year: int
    dead_year: int


class AuthorSchema(AuthorInSchema):
    created_at: datetime
    updated_at: datetime
    books: List[BookSchema]
    books_count: int
