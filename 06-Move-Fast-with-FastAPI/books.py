from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

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
    id: Optional[int] = Field(
        default=None,
        description="Id is not needed on create"
    )
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Pragmatic Programmer",
                "author": "Andrew Hunt",
                "description": "Practical techniques for becoming a better programmer.",
                "rating": 5
            }
        }
    }

        

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
    # new_book = Book(**book_request.dict())
    new_book = Book(**book_request.model_dump())
    Books.append(find_book_id(new_book))
    return new_book


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in Books:
        if book.id == book_id:
            return book

def find_book_id(book: Book):
    if len(Books) > 0:
        book.id = Books[-1].id + 1 # last id in a book
    else:
        book.id = 1
    
    return book