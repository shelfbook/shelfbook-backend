from abc import ABC, abstractmethod

from core.db import database
from schema import AuthorInSchema
from domain import authors


class AuthorRepository:
    @abstractmethod
    async def create(self, author: AuthorInSchema): ...

    @abstractmethod
    async def get_all(self): ...


class DBAuthorRepository(AuthorRepository):
    def __init__(self):
        self.table = authors

    async def create(self, author: AuthorInSchema):
        query = self.table.insert().values(author.dict())
        pk = await database.execute(query)
        return author

    async def get_all(self):
        query = self.table.select()
        objs = await database.fetch_all(query)
        for obj in objs:
            obj.books = {}
            obj.books_count = 0
        return objs
