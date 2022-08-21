from fastapi import APIRouter
from schema import AuthorSchema
from service import CreateAuthorService
from repository import DBAuthorRepository

router = APIRouter(
    prefix='/authors',
    tags=['authors']
)


@router.get('')
async def author_list():
    pass


@router.post(
    path='',
    response_model=AuthorSchema
)
async def author_create(author: AuthorSchema):
    service = CreateAuthorService.new()
    return await service.execute(author)


@router.get('/combiner')
async def author_combiner():
    pass
