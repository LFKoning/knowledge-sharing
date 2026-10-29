"""Managing To Do list with FastAPI."""

import os
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import ValidationError

from data_model import ToDoItem, ToDoStatus

# Folder to store JSON files in.
TODO_FOLDER = Path("todo_items/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


@app.get("/add")
def add_item(description: Annotated[str, Query(min_length=3, max_length=250)]) -> str:
    """Create a new To Do item."""

    # Create a new ToDoItem from a description.
    try:
        todo_item = ToDoItem(description=description)
    except ValidationError:
        raise HTTPException(status_code=422, detail="Invalid description provided")

    # Construct the file name from the item ID.
    filename = f"{todo_item.item_id}.json"

    # Store item as JSON file.
    with open(TODO_FOLDER / filename, "w", encoding="utf8") as json_file:

        # Write the ToDoItem as JSON.
        json_file.write(todo_item.model_dump_json())

    return f"Created TO DO item: {description}"


@app.get("/")
@app.get("/list")
def list_items() -> list[ToDoItem]:
    """Return a list of all To Do items."""
    todo_items = []
    file_paths = TODO_FOLDER.glob("*.json")
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf8") as json_file:
            todo_item = ToDoItem.model_validate_json(json_file.read())
            todo_items.append(todo_item)

    return todo_items


@app.get("/update")
def update_item(item_id: str, status: ToDoStatus) -> str:
    """Set the status of an existing To Do item."""


@app.get("/delete")
def delete_item(item_id: str) -> str:
    """Set the status of an existing To Do item."""
    file_path = TODO_FOLDER / f"{item_id}.json"
    file_paths = TODO_FOLDER.glob("*.json")
    if file_path in file_paths:
        os.remove(file_path)

    return "Deleted TO DO item: {item_id}"
