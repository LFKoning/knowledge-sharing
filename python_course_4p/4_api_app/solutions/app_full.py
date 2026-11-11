"""Streamlit frontend for the to do application."""

import requests
import streamlit as st

API_URL = "http://localhost:8000"


def load_tasks():
    """Return list of tasks from the API."""
    response = requests.get(f"{API_URL}/list", timeout=5)
    if response.status_code != 200:
        st.error("Failed to fetch To Do tasks from the API.")
        return []

    sort_prio = {"High": 0, "Medium": 1, "Low": 2}
    return sorted(
        response.json(),
        key=lambda task: (sort_prio[task["priority"]], task["description"]),
    )


def add_task(task_description, task_priority):
    """Add a new task."""
    requests.get(
        f"{API_URL}/add",
        params={"description": task_description, "priority": task_priority},
        timeout=5,
    )

    # Reload the page to show the added task.
    st.rerun()


def complete_task(task_id):
    """Set task status to complete."""
    requests.get(
        f"{API_URL}/update",
        params={"task_id": task_id, "status": "Completed"},
        timeout=5,
    )


def delete_task(task_id):
    """Delete an existing task."""
    requests.get(
        f"{API_URL}/delete",
        params={"task_id": task_id},
        timeout=5,
    )


TODO_taskS = load_tasks()

# Page settings and title.
st.set_page_config(page_title="TO DO List", layout="wide")
st.title("📝 TO DO List")

st.divider()

# Create three column layout.
column_add, column_active, column_completed = st.columns(3, gap="large")


# Left column: Form to add new tasks.
with column_add:
    st.subheader("Add New Task")
    with st.form("add_task_form", clear_on_submit=True):

        description = st.text_input("Description")
        priority = st.selectbox("Priority", options=["High", "Medium", "Low"], index=1)
        submit = st.form_submit_button("Add task")

        if submit:
            if description:
                add_task(description, priority)
            else:
                st.error("Please enter a description.")


# Left column: Display active tasks.
with column_active:
    st.subheader("Active Tasks")
    for task in TODO_taskS:
        if task["status"] == "Active":
            with st.container(border=True):
                left, right = st.columns([10, 1])
                with left:
                    st.subheader(task["description"])
                with right:
                    st.button(
                        label=">>",
                        key=task["task_id"],
                        on_click=complete_task,
                        kwargs={"task_id": task["task_id"]},
                    )
                st.write(f"{task['priority']} | {task['created_date']}")


# Right column: Display completed tasks.
with column_completed:
    st.subheader("Completed Tasks")
    for task in TODO_taskS:
        if task["status"] == "Completed":
            with st.container(border=True):
                left, right = st.columns([10, 1])
                with left:
                    st.subheader(task["description"])
                with right:
                    st.button(
                        label="X",
                        key=task["task_id"],
                        on_click=delete_task,
                        kwargs={"task_id": task["task_id"]},
                    )
                st.write(f"{task['priority']} | {task['completed_date']}")
