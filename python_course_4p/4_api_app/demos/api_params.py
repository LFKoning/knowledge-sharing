"""FastAPI parameter demo."""

from typing import Literal
from fastapi import FastAPI

TaskStatus = Literal["Active", "Completed"]

app = FastAPI()


@app.get("/delete/{task_id}")
def delete_task(task_id: int) -> str:
    """Delete a task using path parameters."""
    return f"Deleted task: {task_id}"


@app.get("/update")
def update_task(task_id: int, status: TaskStatus) -> str:
    """Update a task status using query parameters."""
    return f"Set status to {status} for task: {task_id}"
