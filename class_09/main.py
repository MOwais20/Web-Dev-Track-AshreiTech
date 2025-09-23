# FastAPI Simple To-Do List Example
# This file demonstrates a basic CRUD API for a To-Do list using FastAPI.
# Students can use this as a starting point to learn about REST APIs and FastAPI features.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

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
    id: str  # Unique identifier for the todo item
    task: str  # Description of the task
    done: bool = False  # Status of the task (default: not done)

# In-memory list to store todos
# In a real app, you would use a database
todos: List[Todo] = [
    # {
    # "id": 1,
    # "task": "Task 1",
    # "done": False
    # },
    #  {
    # "id": 2,
    # "task": "Task 2",
    # "done": False
    # }
    
]

@app.post("/todo/add-item")
def add_item_in_todo(item: Todo):
    todos.append(item)

    print("\nCurrent Todos: ", todos)

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
def delete_item_from_todo(item_id: str):

    if len(todos) > 0:
        for todo_item in todos:

            print("Item ID: ", todo_item.id)

            if todo_item.id == str(item_id):
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
        
@app.put("/todo/update-item")
def update_item_in_todo(item_id: str):
    print("Id: ", item_id, type(item_id))
    for index, todo in enumerate(todos):
        print("Index: ", index, "\n")
        print("Todo Item: ", todos[index], "\n")

        # try:
        if item_id == todo["id"]:
            todos[index]["done"] = True 
            return {
                "message": "Task marked to done.",
                "success": True
            }
            # else:
            #     return {
            #     "message": "Task not marked to done.",
            #     "success": False
            # }
        # except Exception as e:
        #     print("Error", e)
            
           
           
          




# To run this app:


# Tasks
# create an update endpoint to update a todo item
# create a get by id endpoint to get a specific todo item

# 1. pip install fastapi uvicorn pydantic
# 2. uvicorn main:app --reload
# 3. Open http://127.0.0.1:8000/docs for interactive API documentation
