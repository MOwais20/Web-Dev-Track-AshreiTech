from pydantic import BaseModel, Field

"""
This module defines Pydantic models for representing and validating book data.

Classes:
    Book: Represents a book with id, title, author, and price fields.
    BookCreate: Model for creating a new book, requiring title, author, and price.
    BookUpdate: Model for updating book details, allowing optional title, author, and price.

We use Pydantic models to ensure data validation and type enforcement, making it easier to handle and serialize/deserialize data in APIs and applications.

"""

# Why do we need serialize/deserialize and what is it?
# Serialization is the process of converting a Python object (like a Book instance) into a format that can be easily stored or transmitted, such as JSON.
# Deserialization is the reverse process: converting data (like JSON from an API request) back into a Python object.
# This is essential for APIs and web applications, where data needs to be exchanged between different systems in a standard format.




class Book(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., example="The Great Gatsby")
    author: str = Field(..., example="F. Scott Fitzgerald")
    price: float = Field(..., example=19.99)

class BookCreate(BaseModel):
    title: str
    author: str
    price: float

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None
