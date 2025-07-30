from fastapi import APIRouter, HTTPException, Depends
from models import Book, BookCreate, BookUpdate
from auth import verify_token

router = APIRouter(prefix="/books", tags=["books"])

books_db = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", price=19.99),
    Book(id=2, title="1984", author="George Orwell", price=14.99)
]

@router.get("/", response_model=list[Book])
def list_books():
    return books_db

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/", response_model=Book, dependencies=[Depends(verify_token)])
def create_book(book: BookCreate):
    new_id = max([b.id for b in books_db], default=0) + 1
    new_book = Book(id=new_id, **book.dict())
    books_db.append(new_book)
    return new_book

@router.put("/{book_id}", response_model=Book, dependencies=[Depends(verify_token)])
def update_book(book_id: int, book: BookUpdate):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            updated = b.copy(update=book.dict(exclude_unset=True))
            books_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}", dependencies=[Depends(verify_token)])
def delete_book(book_id: int):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            books_db.pop(idx)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
