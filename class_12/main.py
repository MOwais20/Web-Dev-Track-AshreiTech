from hello import app

# This file is a simple wrapper that imports the app from hello.py
# It allows you to run the server with: uvicorn main:app --reload
# While keeping all the application logic in hello.py

# The app object contains:
# 1. FastAPI application instance
# 2. Middleware configuration (CORS, logging)
# 3. API routes (from routes.py)
# 4. Authentication routes (from auth.py)
# 5. Template rendering with Jinja2
# 6. Static file serving

# Run with: uvicorn main:app --reload
