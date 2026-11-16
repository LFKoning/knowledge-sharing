"""Streamlit frontend for the to do application."""

import requests
import streamlit as st

API_URL = "http://localhost:8000"


def load_tasks():
    """Return list of tasks from the API.
    
    Returns
    -------
    list
        List of tasks dicts.
    """
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
    """Add a new task with provided description and priority."""
    requests.get(
        f"{API_URL}/add",
        params={"description": task_description, "priority": task_priority},
        timeout=5,
    )

    # Reload the page to show the added task.
    st.rerun()


def complete_task(task_id):
    """Complete task with the provided task_id."""
    requests.get(
        f"{API_URL}/update",
        params={"task_id": task_id, "status": "Completed"},
        timeout=5,
    )


def delete_task(task_id):
    """Delete task with the provided task_id."""
    requests.get(
        f"{API_URL}/delete",
        params={"task_id": task_id},
        timeout=5,
    )

# Holds the list of tasks, active and complete.
TASK_LIST = load_tasks()

# Page settings and title.
st.set_page_config(page_title="TO DO List", layout="wide")
st.title("📝 TO DO List")

st.divider()

# Create three column layout.
column_add, column_active, column_completed = st.columns(3, gap="large")


# Left column:
with column_add:

    # Header: New Task.
    st.header("New Task")

    # Form for adding tasks.
    with st.form("add_task_form", clear_on_submit=True):

        # Text input for description.
        description = st.text_input("Description")

        # Selectbox for priority (High, Medium, Low).
        priority = st.selectbox("Priority", options=["High", "Medium", "Low"], index=1)

        # Submit button labeled Add Task.
        submit = st.form_submit_button("Add Task")

        # On submit:
        if submit:

            # Check for a valid description.
            if description:

                # Call the add_task function.
                add_task(description, priority)

            else:

                # Display error when no description is provided.
                st.error("Please enter a description.")


# Center column:
with column_active:

    # Header: Active Tasks.
    st.header("Active Tasks")

    # For loop for tasks in TASK_LIST.
    for task in TASK_LIST:

        # Filter active tasks only.
        if task["status"] == "Active":

            # Container with border for a task.
            with st.container(border=True):

                # Two columns with a 10 : 1 ratio.
                task_left, task_right = st.columns((10, 1))

                # Left column:
                with task_left:

                    # Subheader: task description.
                    st.subheader(task["description"])

                # Right column:
                with task_right:

                    # Complete task button.
                    st.button(
                        key=task["task_id"],
                        label = ">>",
                        on_click=complete_task,
                        kwargs={"task_id": task["task_id"]}
                    )


# Right column:
with column_completed:

    # Header: Completed Tasks
    st.header("Completed Tasks")

    # For loop for tasks in TASK_LIST.
    for task in TASK_LIST:

        # Filter completed tasks only.
        if task["status"] == "Completed":

            # Container with border for a task.
            with st.container(border=True):

                # Two columns with a 10 : 1 ratio.
                task_left, task_right = st.columns((10, 1))

                # Left column:
                with task_left:

                    # Subheader: task description.
                    st.subheader(task["description"])

                # Right column:
                with task_right:

                    # Delete task button.
                    st.button(
                        key=task["task_id"],
                        label = "X",
                        on_click=delete_task,
                        kwargs={"task_id": task["task_id"]}
                    )
