from typing import Optional, Union

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int = None
    title: str
    original_title: Optional[str]
    author: Union[int, dict]
    year: int = 2001
