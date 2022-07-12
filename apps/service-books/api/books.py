from typing import Union, List

from fastapi import APIRouter

from schema.book import BookSchema
from service import book_service


books_router = APIRouter()


@books_router.get(
    "/",
    response_model=List[BookSchema],
    responses={"200": {"model": List[BookSchema]}}
)
async def book_list():
    return await book_service.get_all()


@books_router.get(
    "/items/{item_id}",
)
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }
