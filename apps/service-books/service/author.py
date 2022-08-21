from repository import AuthorRepository, DBAuthorRepository
from schema import AuthorInSchema


class BaseAuthorService:
    @classmethod
    def new(cls):
        return cls(DBAuthorRepository())

    def __init__(self, repository: AuthorRepository):
        self.repository = repository


class CreateAuthorService(BaseAuthorService):
    async def execute(self, author: AuthorInSchema) -> AuthorInSchema:
        return await self.repository.create(author)


class ListingAuthorService(BaseAuthorService):
    async def execute(self):
        return await self.repository.get_all()

