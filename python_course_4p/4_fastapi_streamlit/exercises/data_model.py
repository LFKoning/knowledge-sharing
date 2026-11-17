"""Pydantic data model for to do application."""

from uuid import uuid4
from typing import Literal

from pydantic import BaseModel, Field

# Define type for statuses: "Active", or "Completed".
ToDoStatus = ...

# Define type for valid priorities: "High", "Medium", or "Low".
ToDoPriority = ...


# Create a ToDoTask BaseModel with attributes:

# - task_id         Unique ID string from using str(uuid4()).
# - description     Obligatory description as string.
# - priority        Priority with default "Medium".
# - status          Status with default "Active".
