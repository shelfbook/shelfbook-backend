from repository.book import MockBookRepository
from service.book import BookService

book_service = BookService(MockBookRepository())
