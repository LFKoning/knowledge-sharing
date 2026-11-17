"""Pydantic data model for to do application."""

from uuid import uuid4
from typing import Literal

from pydantic import BaseModel, Field

ToDoStatus = Literal["Active", "Completed"]

ToDoPriority = Literal["High", "Medium", "Low"]


class ToDoTask(BaseModel):
    """Basemodel for tasks."""

    task_id: str = Field(default_factory=lambda: str(uuid4()))
    description: str
    priority: ToDoPriority = "Medium"
    status: ToDoStatus = "Active"
