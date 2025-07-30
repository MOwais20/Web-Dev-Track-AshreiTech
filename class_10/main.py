from fastapi import FastAPI
from middleware import log_requests
from routes import router
from auth import auth_router

app = FastAPI()

# Add custom middleware to log incoming requests
app.middleware('http')(log_requests)

# Include the main application routes
app.include_router(router)

# Include authentication-related routes
app.include_router(auth_router)

# Run with: uvicorn main:app --reload
