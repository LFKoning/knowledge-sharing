"""Managing a To Do list with FastAPI."""

import os
from pathlib import Path

from fastapi import FastAPI

from data_model import ToDoTask, ToDoStatus, ToDoPriority

# Folder to store JSON files in.
TODO_FOLDER = Path("todo_list/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


def load_task(task_path: Path) -> ToDoTask:
    """Load a ToDoTask from a JSON file."""
    with open(task_path, "r", encoding="utf8") as task_file:

        # Read JSON content from file.
        task_json = task_file.read()

        # Validate JSON against ToDoTask BaseModel.
        return ToDoTask.model_validate_json(task_json)


def store_task(todo_task: ToDoTask) -> None:
    """Store a ToDoTask as a JSON file."""

    # Construct the file path from the task ID.
    task_path = TODO_FOLDER / f"{todo_task.task_id}.json"

    # Open JSON-file in the TODO_FOlDER.
    with open(task_path, "w", encoding="utf8") as task_file:
        # Dump the ToDoTask as JSON.
        task_json = todo_task.model_dump_json()
        task_file.write(task_json)


@app.get("/add")
def add_task(
    description: str,
    priority: ToDoPriority,
) -> str:
    """Create a new task."""
    task = ToDoTask(description=description, priority=priority)
    store_task(task)

    return f"Created task: {description}"


@app.get("/")
@app.get("/list")
def list_tasks() -> list[ToDoTask]:
    """Return a list of all tasks."""

    # List all JSON-files in the TODO_FOLDER using glob().
    
    # Load all JSON-files into the tasks list.
    task_list = []
    for task_path in task_paths:

        # Load the JSON-file as ToDoTask.
    
        # Append ToDoTask to the list.
    
    # Return the task list.
    return task_list


@app.get("/update")
def update_task(task_id: str, status: ToDoStatus) -> str:
    """Set the status of an existing task."""

    # Construct the file path from the provided task ID.
    
    # Load the task from disk.
    
    # Change the task status.

    # Store the updated task to disk.

    return f"Set status to {status} for task: {task_id}"


@app.get("/delete")
def delete_task(task_id: str) -> str:
    """Delete an existing task."""

    # Construct the file path from the provided task ID.

    # Delete the JSON file.

    return f"Deleted task: {task_id}"
