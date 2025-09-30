# FastAPI Simple To-Do List Example
# This file demonstrates a basic CRUD API for a To-Do list using FastAPI.
# Students can use this as a starting point to learn about REST APIs and FastAPI features.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

import os
from pymongo import MongoClient
from bson import ObjectId


from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

client = MongoClient(os.getenv("DATABASE_URL"))
DB = client[str(os.getenv("DB_NAME"))]

# Create FastAPI app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Define the data model for a Todo item
class Todo(BaseModel): # Object representing a To-Do item
    user_id: str  # Unique identifier for the user
    task: str  # Description of the task
    done: bool = False  # Status of the task (default: not done)

@app.post("/todo/add-item")
def add_item_in_todo(item: Todo):

    # Database insertion
    DB.todos.insert_one(dict(item))

    return {
        "message": "Item added successfully",
        "item": item,
        "success": True
    }

@app.get("/todo/get-items")
def get_items_from_todo(user_id: str):

    todos_items = []
    
    todos_from_db = DB.todos.find({
        "user_id": user_id
    })

    for todo in todos_from_db:
        todo["_id"] = str(todo["_id"])  # Convert ObjectId to string
        todos_items.append(todo)

    return {
        "message": "Items retrieved successfully",
        "items": todos_items,
        "total_items": len(todos_items),
        "success": True
    }

@app.delete("/todo/delete-item")
def delete_item_from_todo(item_id: str):

    response = DB.todos.delete_one({
        "_id": ObjectId(item_id)
    })
    if response.deleted_count == 1:
        return {
            "message": "Item deleted successfully",
            "success": True
        }
    else:
        return {
            "message": "Item not found",
            "success": False
        }

@app.put("/todo/update-item")
def update_item_in_todo(item_id: str):
    response = DB.todos.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"done": True}}
    )
    if response.matched_count == 1:
        return {
            "message": "Item updated successfully",
            "success": True
        }
    else:
        return {
            "message": "Item not found",
            "success": False
        }

@app.put("/todo/update-item-task")
def update_item_task(item_id: str, task: str):
    response = DB.todos.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"task": task}}
    )
    if response.matched_count == 1:
        return {
            "message": "Item updated successfully",
            "success": True
        }
    else:
        return {
            "message": "Item not found",
            "success": False
        }
    
# To run this app:
# 1. pip install -r requirements.txt
# 2. uvicorn main:app --reload
# 3. Open http://127.0.0.1:8000/docs for interactive API documentation

# TASKS

# 1. User Sign Up
# - Create a User model with fields: username, email, password.
# - Add a POST endpoint /user/signup to register a new user.
# - Return success message and user info (excluding password).

# 2. User Sign In
# - Add a POST endpoint /user/signin to authenticate user.
# - Accept username/email and password.
# - Verify password against stored.
# - Return success message.

# 3. CRUD for Todo
# - Create: Already implemented as /todo/add-item.
# - Read: Already implemented as /todo/get-items.
# - Update: Already implemented as /todo/update-item and /todo/update-item-task.
# - Delete: Already implemented as /todo/delete-item.