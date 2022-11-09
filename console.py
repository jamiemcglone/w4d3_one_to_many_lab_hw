import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Stephen", "King")
author2 = Author("Ernest", "Hemingway")

author_repository.save(author1)
author_repository.save(author2)

book1 = Book("The Shining", author1)
book2 = Book("The Sun Also Rises", author2)

book_repository.save(book1)
book_repository.save(book2)

pdb.set_trace()
