"""Managing To Do list with FastAPI."""

from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import ValidationError

from data_model import ToDoItem

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
