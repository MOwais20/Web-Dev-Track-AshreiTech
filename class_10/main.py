from fastapi import FastAPI
from middleware import log_requests, allow_only_POST_methods
from routes import router
from auth import auth_router

app = FastAPI()

# Add custom middleware to log incoming requests
app.middleware('http')(allow_only_POST_methods)

# Include the main application routes
app.include_router(router)

# # Include authentication-related routes
app.include_router(auth_router)

# @app.get("/")
# def show_msg():
#     return {
#         "messgae": "Heeloo, Welcome to our server"
#     }

# Run with: uvicorn main:app --reload
