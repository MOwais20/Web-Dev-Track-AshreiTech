from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from middleware import log_requests
from routes import router, books_db
from models import Book, BookCreate, BookUpdate
from auth import auth_router, verify_token
import os

# Create the FastAPI application instance
app = FastAPI()

# ==========================================
# MIDDLEWARE CONFIGURATION
# ==========================================

# Add CORS middleware to allow cross-origin requests (needed for frontend)
app.add_middleware(
    CORSMiddleware,
    # Allow requests from any origin (can be restricted in production)
    allow_origins=["*"],
    # Allow credentials to be sent with requests (cookies, auth headers)
    allow_credentials=True,
    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],
    # Allow all headers in requests
    allow_headers=["*"],
)

# Add custom middleware to log incoming requests
# This middleware is defined in middleware.py
app.middleware('http')(log_requests)

# ==========================================
# ROUTER CONFIGURATION
# ==========================================

# Include the API routes from routes.py
# This gives us endpoints for CRUD operations on books
app.include_router(router)

# Include authentication-related routes from auth.py
# This gives us endpoints for login and token verification
app.include_router(auth_router)

# ==========================================
# STATIC FILES AND TEMPLATES CONFIGURATION
# ==========================================

# Mount the static files directory to serve CSS, JS, images, etc.
# This makes files in the "static" folder available at the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
# This creates a templates object that can render HTML templates from the "templates" directory
templates = Jinja2Templates(directory="templates")

# ==========================================
# WEB ROUTES FOR HTML PAGES
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the main page with Jinja2 template
    
    This route renders the index.html template and passes the book list to it
    The 'request' parameter is required for all template responses
    """
    return templates.TemplateResponse(
        "index.html",  # The template file to render
        {"request": request, "books": books_db}  # The context data to pass to the template
    )

@app.get("/books/", response_class=HTMLResponse, name="list_books_page")
async def list_books_page(request: Request):
    """
    List all books with Jinja2 template
    
    This route renders the index.html template which displays all books
    We use 'name=' to give this route a name that can be referenced in templates
    """
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "books": books_db}
    )

@app.get("/books/{book_id}", response_class=HTMLResponse)
async def get_book_page(request: Request, book_id: int):
    """
    Get a specific book with Jinja2 template
    
    This route renders the book_detail.html template for a specific book
    It first finds the book by ID, then passes it to the template
    """
    # Find the book with the given ID
    for book in books_db:
        if book.id == book_id:
            # Render the book detail template with the book data
            return templates.TemplateResponse(
                "book_detail.html", 
                {"request": request, "book": book}
            )
    # If book not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/new", response_class=HTMLResponse, name="create_book_page")
async def create_book_form(request: Request):
    """
    Show form to create a new book
    
    This route renders the book_form.html template without a book object
    The template adapts to show a form for creating a new book
    """
    return templates.TemplateResponse(
        "book_form.html", 
        {"request": request}  # No book data, so the form will be empty
    )

@app.get("/books/{book_id}/edit", response_class=HTMLResponse, name="update_book_page")
async def update_book_form(request: Request, book_id: int):
    """
    Show form to edit an existing book
    
    This route renders the book_form.html template with a book object
    The template adapts to show a form pre-filled with the book's data
    """
    # Find the book with the given ID
    for book in books_db:
        if book.id == book_id:
            # Render the form template with the book data
            return templates.TemplateResponse(
                "book_form.html", 
                {"request": request, "book": book}
            )
    # If book not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Book not found")

# ==========================================
# ERROR HANDLERS
# ==========================================

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    """
    Custom handler for 404 Not Found errors
    
    This renders a friendly error page instead of returning JSON error responses
    """
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "message": "The requested resource was not found",
            "status_code": 404
        },
        status_code=404
    )

@app.exception_handler(500)
async def server_error_handler(request: Request, exc: Exception):
    """
    Custom handler for 500 Internal Server Error
    
    This renders a friendly error page for server errors
    """
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "message": "An internal server error occurred",
            "status_code": 500
        },
        status_code=500
    )

# ==========================================
# MISCELLANEOUS ROUTES
# ==========================================

@app.get("/favicon.ico")
def get_favicon():
    """
    Serve favicon.ico file
    
    This special route handles requests for favicon.ico, which browsers automatically request
    """
    return FileResponse(
        os.path.join("static", "favicon.ico"),
        headers={"Content-Disposition": "inline"}
    )

# ==========================================
# RUNNING THE APPLICATION
# ==========================================

# Run with: uvicorn hello:app --reload
# The --reload flag makes the server restart when code changes
# This is useful during development
