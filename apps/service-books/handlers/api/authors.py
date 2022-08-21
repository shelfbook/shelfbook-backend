from fastapi import APIRouter


router = APIRouter(
    prefix='/authors',
    tags=['authors']
)


@router.get('')
async def author_list():
    pass


@router.post('')
async def author_create():
    pass


@router.get('/combiner')
async def author_combiner():
    pass
