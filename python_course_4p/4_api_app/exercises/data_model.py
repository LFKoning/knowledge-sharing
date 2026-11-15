"""Pydantic data model for to do application."""

from uuid import uuid4
import datetime as dt
from typing import Literal

from pydantic import BaseModel, Field


# Create a ToDoTask BaseModel with attributes:

# - task_id         Unique ID string from using uuid4().
# - description     Obligatory description as string.
# - priority        Priority with options: "High", "Medium", or "Low".
# - status          Status with options "Active", or "Completed".
# - created_date    Current datetime formatted as string.
