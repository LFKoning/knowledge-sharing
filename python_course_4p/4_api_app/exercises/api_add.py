"""Managing To Do list with FastAPI."""

from pathlib import Path

from fastapi import FastAPI

from data_model import ToDoTask, ToDoPriority

# Set up a folder to store JSON files.
TODO_FOLDER = Path("todo_list/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


@app.get("/add")
def add_task(description: str, priority: ToDoPriority) -> str:
    """Create a new task."""

    # Create a new ToDoTask from the description and priority.
    task = ...

    # Construct the file path from the task ID.
    task_path = TODO_FOLDER / f"{...}.json"

    # Open a JSON-file to store the ToDoTask.

        # Convert the ToDoTask to JSON with model_dump_json().

        # Write JSON to the file.

    return f"Created task: {description}"
