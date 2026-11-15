"""Managing To Do list with FastAPI."""

from pathlib import Path

from fastapi import FastAPI

from data_model import ToDoTask, ToDoPriority

# Folder to store JSON files in.
TODO_FOLDER = Path("todo_list/")
TODO_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


@app.get("/add")
def add_item(description: str, priority: ToDoPriority) -> str:
    """Create a new task."""

    # Create a new ToDoTask from the description and priority.
    task = ToDoTask(description=description, priority=priority)

    # Construct the file path from the task ID.
    task_path = TODO_FOLDER / f"{task.task_id}.json"

    # Open a JSON-file to store the ToDoTask.
    with open(task_path, "w", encoding="utf8") as json_file:

        # Convert the ToDoTask to JSON with model_dump_json().
        task_json = task.model_dump_json()

        # Write JSON to the file.
        json_file.write(task_json)

    return f"Created task: {description}"
