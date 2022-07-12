from fastapi import APIRouter
from api.books import books_router

router = APIRouter()
router.include_router(books_router)
