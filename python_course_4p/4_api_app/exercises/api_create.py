"""Managing To Do list with FastAPI."""

from pathlib import Path

from fastapi import FastAPI

from data_model import ToDoItem

# Set up a folder to store JSON files.
TODO_FOLDER = Path("todo_items/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


@app.get("/add")
def add_item(description: str) -> str:
    """Create a new To Do item."""

    # Create a new ToDoItem from the description.
    todo_item = ...

    # Construct the file name from the item ID.
    filename = f"{item id here}.json"
    
    # Store item as JSON file.
    with open(TODO_FOLDER / filename, "w", encoding="utf8") as json_file:
        
        # Write the ToDoItem as JSON.

    return f"Created TO DO item: {description}"
