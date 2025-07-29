# FastAPI Simple To-Do List Example
# This file demonstrates a basic CRUD API for a To-Do list using FastAPI.
# Students can use this as a starting point to learn about REST APIs and FastAPI features.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Create FastAPI app instance
app = FastAPI()

# Define the data model for a Todo item
class Todo(BaseModel): # Object representing a To-Do item
    id: int  # Unique identifier for the todo item
    task: str  # Description of the task
    done: bool = False  # Status of the task (default: not done)


# In-memory list to store todos
# In a real app, you would use a database
todos: List[Todo] = []

@app.post("/todo/add-item")
def add_item_in_todo(item: Todo):
    todos.append(item)
    return {
        "message": "Item added successfully",
        "item": item,
        "success": True
    }

@app.get("/todo/get-items")
def get_items_from_todo():
    return {
        "message": "Items retrieved successfully",
        "items": todos,
        "total_items": len(todos),
        "success": True
    }

@app.delete("/todo/delete-item")
def delete_item_from_todo(item_id: int):
    if len(todos) > 0:
        for todo_item in todos:
            
            print(todo_item, item_id)
            
            if todo_item.id == item_id:
                todos.remove(todo_item)
                return {
                    "message": "Item deleted successfully",
                    "item": todo_item,
                    "success": True
                }
            else:
                return {
                    "message": "Item not found / matched",
                    "success": False
                }
    else:
        return {
            "message": "No items found in the To-Do list",
            "success": False
        }
    

# Create a new todo item
# @app.post("/todos/", response_model=Todo)
# def add_todo(todo: Todo):
#     todos.append(todo)
#     return todo

# Get all todo items
# @app.get("/todos/", response_model=List[Todo])
# def get_todos():
#     return todos

# # Update an existing todo item by id
# @app.put("/todos/{todo_id}", response_model=Todo)
# def update_todo(todo_id: int, todo: Todo):
#     for idx, t in enumerate(todos):
#         if t.id == todo_id:
#             todos[idx] = todo
#             return todo
#     return {"error": "Todo not found"}

# Delete a todo item by id
# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):
#     global todos
#     todos = [t for t in todos if t.id != todo_id]
#     return {"message": "Todo deleted"}

# To run this app:





# python -m venv classenv
# 1. pip install fastapi uvicorn pydantic
# 2. uvicorn app:app --reload
# 3. Open http://127.0.0.1:8000/docs for interactive API documentation
