"""Pydantic data model for to do application."""

from uuid import uuid4
import datetime as dt
from typing import Literal

from pydantic import BaseModel, Field

ToDoStatus = Literal["Active", "Completed"]

ToDoPriority = Literal["High", "Medium", "Low"]


class ToDoTask(BaseModel):
    """Basemodel for tasks."""

    task_id: str = Field(default_factory=lambda: str(uuid4()))
    description: str = Field(min_length=3, max_length=250)
    priority: ToDoPriority = "Medium"
    status: ToDoStatus = "Active"
    created_date: str = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    completed_date: str | None = None
