/**
 * script.js - JavaScript for the Book Library App
 * This file handles API interactions and dynamic content updates
 */

// Wait for the DOM to be fully loaded before running code
document.addEventListener('DOMContentLoaded', function() {
    
    // ======= VARIABLES AND CONSTANTS =======
    
    // Store the authentication token
    let authToken = '';
    
    // DOM element references (using const for elements that won't be reassigned)
    const loginBtn = document.getElementById('login-btn');
    const tokenInput = document.getElementById('token-input');
    const authStatus = document.getElementById('auth-status');
    const searchInput = document.getElementById('search');
    const editModal = document.getElementById('edit-modal');
    const closeBtn = document.querySelector('.close-btn');
    
    // Conditionally get elements that may not be present on all pages
    const addBookForm = document.getElementById('add-book-form');
    const editBookForm = document.getElementById('edit-book-form');
    const booksContainer = document.querySelector('.books-container');
    const loadingMessage = document.getElementById('loading-message');
    
    // ======= EVENT LISTENERS =======
    
    // Login button click handler
    if (loginBtn) {
        loginBtn.addEventListener('click', handleLogin);
    }
    
    // Add book form submission
    if (addBookForm) {
        addBookForm.addEventListener('submit', handleAddBook);
    }
    
    // Edit book form submission
    if (editBookForm) {
        editBookForm.addEventListener('submit', handleEditBook);
    }
    
    // Close modal when clicking the X button
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            editModal.style.display = 'none';
        });
    }
    
    // Close modal when clicking outside the modal content
    if (editModal) {
        window.addEventListener('click', (event) => {
            if (event.target === editModal) {
                editModal.style.display = 'none';
            }
        });
    }
    
    // Search input handler
    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
    }
    
    // ======= INITIALIZATION =======
    
    // With Jinja templates, we don't need to load books via JavaScript initially
    // as they're rendered server-side. This function is kept for reference or if
    // dynamic reloading is needed.
    
    // ======= FUNCTION DEFINITIONS =======
    
    /**
     * Handles the login process
     * @param {Event} event - The event object
     */
    function handleLogin(event) {
        // Prevent form submission
        event.preventDefault();
        
        // Get the token from the input field
        const token = tokenInput.value.trim();
        
        if (!token) {
            // Alert the user if no token was entered
            alert('Please enter a token');
            return;
        }
        
        // Store the token for future API calls
        authToken = token;
        localStorage.setItem('authToken', token); // Save token in local storage
        
        // Update the UI to show authenticated state
        authStatus.textContent = 'Authenticated';
        authStatus.style.color = '#2ecc71'; // Green color
        
        // Optional: You could verify the token here with an API call
        fetch('/login', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.access_token && data.access_token === token) {
                // Token is valid
                console.log('Token verified');
            }
        })
        .catch(error => {
            console.error('Token verification error:', error);
        });
    }
    
    // Check if we have a stored token and restore it
    if (tokenInput) {
        const storedToken = localStorage.getItem('authToken');
        if (storedToken) {
            tokenInput.value = storedToken;
            authToken = storedToken;
            authStatus.textContent = 'Authenticated';
            authStatus.style.color = '#2ecc71';
        }
    }
    
    /**
     * Handles adding a new book
     * @param {Event} event - The submit event
     */
    async function handleAddBook(event) {
        // Prevent the form from submitting normally
        event.preventDefault();
        
        // Check if user is authenticated
        if (!authToken) {
            alert('Please log in first');
            return;
        }
        
        try {
            // Get form data
            const title = document.getElementById('title').value;
            const author = document.getElementById('author').value;
            const price = parseFloat(document.getElementById('price').value);
            
            // Create book object
            const newBook = { title, author, price };
            
            // Send POST request to API
            const response = await fetch('/books/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(newBook)
            });
            
            // Check if request was successful
            if (!response.ok) {
                throw new Error('Failed to add book');
            }
            
            // Parse the response (the newly created book)
            const book = await response.json();
            
            // Redirect to the book list page
            window.location.href = '/books/';
            
        } catch (error) {
            console.error('Error adding book:', error);
            alert('Error adding book: ' + error.message);
        }
    }
    
    /**
     * Opens the edit modal with book data
     * @param {Object} book - The book object to edit
     */
    function openEditModal(book) {
        // Fill the form with the book data
        document.getElementById('edit-book-id').value = book.id;
        document.getElementById('edit-title').value = book.title;
        document.getElementById('edit-author').value = book.author;
        document.getElementById('edit-price').value = book.price;
        
        // Show the modal
        editModal.style.display = 'block';
    }
    
    /**
     * Handles editing a book
     * @param {Event} event - The submit event
     */
    async function handleEditBook(event) {
        // Prevent the form from submitting normally
        event.preventDefault();
        
        // Check if user is authenticated
        if (!authToken) {
            alert('Please log in first');
            return;
        }
        
        try {
            // Get form data
            const bookId = document.getElementById('edit-book-id').value;
            const title = document.getElementById('edit-title').value;
            const author = document.getElementById('edit-author').value;
            const price = parseFloat(document.getElementById('edit-price').value);
            
            // Create book update object
            const bookUpdate = { title, author, price };
            
            // Send PUT request to API
            const response = await fetch(`/books/${bookId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(bookUpdate)
            });
            
            // Check if request was successful
            if (!response.ok) {
                throw new Error('Failed to update book');
            }
            
            // Parse the response (the updated book)
            const book = await response.json();
            
            // Close the modal
            editModal.style.display = 'none';
            
            // Refresh the page
            window.location.reload();
            
        } catch (error) {
            console.error('Error updating book:', error);
            alert('Error updating book: ' + error.message);
        }
    }
    
    /**
     * Handles deleting a book
     * @param {number} bookId - The ID of the book to delete
     */
    async function handleDeleteBook(bookId) {
        // Ask for confirmation
        if (!confirm('Are you sure you want to delete this book?')) {
            return;
        }
        
        // Check if user is authenticated
        if (!authToken) {
            alert('Please log in first');
            return;
        }
        
        try {
            // Send DELETE request to API
            const response = await fetch(`/books/${bookId}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${authToken}`
                }
            });
            
            // Check if request was successful
            if (!response.ok) {
                throw new Error('Failed to delete book');
            }
            
            // Get the response
            const result = await response.json();
            
            // Show success message
            alert('Book deleted successfully');
            
            // Redirect to books page or reload current page
            if (window.location.pathname === '/books/' || window.location.pathname === '/') {
                window.location.reload();
            } else {
                window.location.href = '/books/';
            }
            
        } catch (error) {
            console.error('Error deleting book:', error);
            alert('Error deleting book: ' + error.message);
        }
    }
    
    /**
     * Handles searching for books
     * @param {Event} event - The input event
     */
    function handleSearch(event) {
        const searchTerm = event.target.value.toLowerCase();
        
        // Get all book cards except the template
        const bookCards = document.querySelectorAll('.book-card:not(.template)');
        
        // Loop through each book card
        bookCards.forEach(card => {
            // Get the title and author text
            const title = card.querySelector('.book-title').textContent.toLowerCase();
            const author = card.querySelector('.book-author').textContent.toLowerCase();
            
            // Check if the search term is in the title or author
            if (title.includes(searchTerm) || author.includes(searchTerm)) {
                card.style.display = 'block'; // Show the card
            } else {
                card.style.display = 'none'; // Hide the card
            }
        });
    }
});
