from repository.book import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()
