"""FastAPI parameter demo."""

from typing import Literal
from fastapi import FastAPI

ToDoStatus = Literal["Active", "Completed"]
ToDoPriority = Literal["High", "Medium", "Low"]


# Dummy task list.
TASK_LIST = [
    {"task_id": 1, "description": "Task 1", "priority": "High", "status": "Completed"},
    {"task_id": 2, "description": "Task 2", "priority": "Medium", "status": "Active"},
    {"task_id": 3, "description": "Task 3", "priority": "Low", "status": "Completed"},
    {"task_id": 4, "description": "Task 4", "priority": "Low", "status": "Active"},
]

app = FastAPI()


@app.get("/list")
def list_tasks(status: ToDoStatus = None, priority: ToDoPriority = None) -> list:
    """List tasks filtered by status and priority."""
    filtered = TASK_LIST
    if status:
        filtered = [task for task in filtered if task["status"] == status]
    if priority:
        filtered = [task for task in filtered if task["priority"] == priority]

    return filtered
