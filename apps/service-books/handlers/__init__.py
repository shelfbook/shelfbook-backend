from fastapi import APIRouter
from handlers.api import books_router, author_router

router = APIRouter()
router.include_router(books_router)
router.include_router(author_router)
