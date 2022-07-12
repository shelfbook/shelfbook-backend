from abc import ABCMeta, abstractmethod


class BookRepository:
    @abstractmethod
    async def get_all(self): ...

    @abstractmethod
    async def get_by_id(self, book_id: int): ...

    @abstractmethod
    async def create(self, name, author_id): ...

    @abstractmethod
    async def delete(self, book_id): ...


class MockBookRepository(BookRepository):
    async def get_all(self):
        return [
            {"id": 1, "title": "Американская трагедия", "author": "Драйзер", "year": 2000},
            {"id": 2, "title": "Война и мир", "author": "Толстой"}
        ]
