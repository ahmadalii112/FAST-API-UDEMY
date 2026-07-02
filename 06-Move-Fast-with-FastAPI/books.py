from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

        

Books = [
    Book(1, 'Mastering FastAPI', 'Sebastián Ramírez', 'Learn how to build modern APIs with FastAPI.', 5),
    Book(2, 'Learning Python', 'Mark Lutz', 'A comprehensive guide to Python programming.', 5),
    Book(3, 'Effective SQL', 'John L. Viescas', 'Best practices for writing efficient SQL queries.', 4),
    Book(4, 'Docker Deep Dive', 'Nigel Poulton', 'Understand Docker containers and deployment.', 5),
    Book(5, 'Building REST APIs', 'Brenda Jin', 'Design and develop RESTful web services.', 4),
    Book(6, 'Clean Architecture', 'Robert C. Martin', 'Learn software architecture and design principles.', 5),
]


@app.get("/books")
async def read_all_books():
    return Books


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    """ 
    {"id": 7,"title": "The Pragmatic Programmer","author": "Andrew Hunt","description": "Practical techniques for becoming a better programmer","rating": 4} 
    """
    new_book = Book(**book_request.dict())
    # new_book = Book(**book_request.model_dump())
    Books.append(book_request)