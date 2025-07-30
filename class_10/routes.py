from fastapi import APIRouter, HTTPException, Depends
from models import Book, BookCreate, BookUpdate
from auth import verify_token

# Create a router for book-related endpoints
router = APIRouter(prefix="/books", tags=["books"])

# In-memory database of books (for demonstration purposes)
books_db = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", price=19.99),
    Book(id=2, title="1984", author="George Orwell", price=14.99)
]

@router.get("/", response_model=list[Book])
def list_books():
    """
    Get a list of all books.
    """
    return books_db

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    Retrieve a book by its ID.
    Raises 404 if not found.
    """
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/", response_model=Book, dependencies=[Depends(verify_token)])
def create_book(book: BookCreate):
    """
    Create a new book.
    Requires authentication.
    """
    # Generate a new ID for the book
    new_id = max([b.id for b in books_db], default=0) + 1
    # Create a new Book instance
    new_book = Book(id=new_id, **book.dict())
    # Add the new book to the database
    books_db.append(new_book)
    return new_book

@router.put("/{book_id}", response_model=Book, dependencies=[Depends(verify_token)])
def update_book(book_id: int, book: BookUpdate):
    """
    Update an existing book by ID.
    Only updates fields provided.
    Requires authentication.
    """
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            # Update only the fields that are set
            updated = b.copy(update=book.dict(exclude_unset=True))
            books_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}", dependencies=[Depends(verify_token)])
def delete_book(book_id: int):
    """
    Delete a book by its ID.
    Requires authentication.
    """
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            books_db.pop(idx)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
