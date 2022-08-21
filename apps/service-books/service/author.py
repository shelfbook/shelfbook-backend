from repository import AuthorRepository, DBAuthorRepository
from schema import AuthorSchema


class CreateAuthorService:
    @classmethod
    def new(cls):
        return cls(DBAuthorRepository())

    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    async def execute(self, author: AuthorSchema) -> AuthorSchema:
        return await self.repository.create(author)
