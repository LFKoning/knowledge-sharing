"""FastAPI parameter demo."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/greet/{name}/{last_name}")
def greet(name: str, last_name: str) -> str:
    """Greet using path parameters."""
    return f"Hello {name} {last_name}!"


@app.get("/hello")
def hello(name: str, last_name: str) -> str:
    """Greet using query parameters."""
    return f"Hello {name} {last_name}!"


class User(BaseModel):
    """Pydantic BaseModel for a user."""

    name: str
    last_name: str


@app.post("/wave")
def wave(user: User) -> str:
    """Greet using request body."""
    return f"Hello {user.name} {user.last_name}!"
