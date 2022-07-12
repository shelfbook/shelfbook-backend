from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int = None
    title: str
    author: str = None
    year: int = 2001
