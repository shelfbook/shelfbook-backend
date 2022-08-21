from abc import ABC, abstractmethod

from core.db import database
from schema import AuthorSchema
from domain import authors


class AuthorRepository:
    @abstractmethod
    async def create(self, author: AuthorSchema): ...


class DBAuthorRepository(AuthorRepository):
    async def create(self, author: AuthorSchema):
        query = authors.insert().values(author.dict())
        author_id = await database.execute(query)
        return author
