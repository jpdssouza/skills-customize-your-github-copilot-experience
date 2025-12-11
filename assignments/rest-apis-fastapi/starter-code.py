"""
FastAPI REST API Starter Code

This starter code provides a foundation for building a REST API with FastAPI.
Complete the tasks in the README.md file to build a full CRUD application.

Requirements to install:
- pip install fastapi
- pip install uvicorn

To run this application:
- uvicorn starter_code:app --reload
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List

# TODO: Create your FastAPI app instance here
# app = FastAPI()

# TODO: Define a Pydantic model for your resource
# Example: For a book API, you might have:
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     year: int


# TODO: Create an in-memory data structure to store items
# Example:
# books_db = [
#     {"id": 1, "title": "Python Basics", "author": "John Doe", "year": 2023},
#     {"id": 2, "title": "Web Development", "author": "Jane Smith", "year": 2024}
# ]


# TODO: Implement your GET endpoints
# GET /items - Return all items
# GET /items/{item_id} - Return a specific item by ID


# TODO: Implement your POST endpoint
# POST /items - Create a new item


# TODO: Implement your PUT endpoint
# PUT /items/{item_id} - Update an existing item


# TODO: Implement your DELETE endpoint
# DELETE /items/{item_id} - Delete an item


# TODO: Add query parameters for filtering and pagination
# GET /items?skip=0&limit=10
# GET /items?author=John


if __name__ == "__main__":
    # Run with: uvicorn starter_code:app --reload
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
