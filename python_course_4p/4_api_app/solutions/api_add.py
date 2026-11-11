"""Managing To Do list with FastAPI."""

from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import ValidationError

from data_model import ToDoTask, ToDoPriority

# Folder to store JSON files in.
TODO_FOLDER = Path("todo_items/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


@app.get("/add")
def add_item(description: str, priority: ToDoPriority) -> str:
    """Create a new To Do item."""

    # Create a new ToDoTask from the description and priority.
    try:
        todo_item = ToDoTask(description=description, priority=priority)
    except ValidationError:
        raise HTTPException(status_code=422, detail="Invalid description provided.")

    # Construct the file name from the item ID.
    filename = f"{todo_item.item_id}.json"

    # Store item as JSON file.
    with open(TODO_FOLDER / filename, "w", encoding="utf8") as json_file:

        # Write the ToDoItem as JSON.
        json_file.write(todo_item.model_dump_json())

    return f"Created TO DO item: {description}"
