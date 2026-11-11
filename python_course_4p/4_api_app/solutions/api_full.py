"""Managing a To Do list with FastAPI."""

import os
import datetime as dt
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from data_model import ToDoTask, ToDoStatus, ToDoPriority

# Folder to store JSON files in.
TODO_FOLDER = Path("todo_tasks/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


def load_task(task_path: Path) -> ToDoTask:
    """Load ToDoTask from a JSON-file."""
    with open(task_path, "r", encoding="utf8") as task_file:
        # Read JSON content from file.
        task_json = task_file.read()

        # Validate JSON against ToDoTask BaseModel.
        return ToDoTask.model_validate_json(task_json)


def store_task(todo_task: ToDoTask) -> None:
    """Store ToDoTask as a JSON-file."""
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

    # Create a ToDoTask from the provided description and priority.
    try:
        task = ToDoTask(description=description, priority=priority)
    except ValidationError as error:
        raise HTTPException(
            status_code=422, detail="Invalid description or priority provided"
        ) from error

    # Store the task to disk.
    store_task(task)

    return f"Created task: {description}"


@app.get("/")
@app.get("/list")
def list_tasks() -> list[ToDoTask]:
    """Return a list of all tasks."""

    # Get a list of all JSON-files in the TODO_FOLDER.
    task_paths = TODO_FOLDER.glob("*.json")

    # Load all JSON-files into the tasks list.
    tasks = []
    for task_path in task_paths:
        # Load the JSON-file as ToDoTask.
        task = load_task(task_path)

        # Append ToDoTask to the list.
        tasks.append(task)

    # Return the tasks list.
    return tasks


@app.get("/update")
def update_task(task_id: str, status: ToDoStatus) -> str:
    """Set the status of an existing task."""
    # Read the task from disk.
    file_path = TODO_FOLDER / f"{task_id}.json"
    task = load_task(file_path)

    # Change status and completed datetime.
    task.status = status
    task.completed_date = dt.datetime.now()

    # Store updated task to disk.
    store_task(task)

    return f"Set status to {status} for task: {task_id}"


@app.get("/delete")
def delete_task(task_id: str) -> str:
    """Delete an existing task."""
    # Get a list of all existing tasks.
    file_paths = TODO_FOLDER.glob("*.json")

    # Check if task exists, delete if so.
    file_path = TODO_FOLDER / f"{task_id}.json"
    if file_path in file_paths:
        os.remove(file_path)

    return f"Deleted task: {task_id}"
