from typing import List

from fastapi import APIRouter
from schema import AuthorInSchema, AuthorSchema
from service import CreateAuthorService, ListingAuthorService


router = APIRouter(
    prefix='/authors',
    tags=['authors']
)


@router.get(
    '',
    response_model=List[AuthorSchema],
)
async def author_list():
    service = ListingAuthorService.new()
    listing = await service.execute()
    return listing


@router.post(
    path='',
    response_model=AuthorInSchema
)
async def author_create(author: AuthorInSchema):
    service = CreateAuthorService.new()
    return await service.execute(author)


@router.get('/combiner')
async def author_combiner():
    pass
