from typing import List
from fastapi import APIRouter
from schema import BookSchema, ConfirmerSchema, BookCombineSchema


router = APIRouter(
    prefix='/books',
    tags=["books"]
)


@router.get(
    '',
    response_model=List[BookSchema],
    responses={"200": {"model": List[BookSchema]}},
)
async def book_list():
    """List of book"""
    # return await book_service.get_all()
    pass


@router.post(
    '',
)
def create_book(book: BookSchema):
    return {
        "item_id": "item_id",
        "q": "q"
    }


@router.post("/{book_id}/confirmer")
def book_confirmer(book_id: int, confirmer: ConfirmerSchema):
    return {
        "item_id": "item_id",
        "q": "q"
    }


@router.patch("/{book_id}")
def update_book():
    pass


@router.post("/combiner")
def books_combiner(combiner: BookCombinerSchema):
    """Combine books"""
    pass