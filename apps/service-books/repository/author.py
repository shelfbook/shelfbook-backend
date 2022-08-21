from abc import ABC, abstractmethod
from schema import AuthorSchema


class AuthorRepository:
    @abstractmethod
    async def create(self, author: AuthorSchema): ...


class DBAuthorRepository(AuthorRepository):
    async def create(self, author: AuthorSchema):
        print(author)
        return author
