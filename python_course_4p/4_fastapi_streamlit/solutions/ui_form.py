"""Layout for the To Do list app in Streamlit."""

import streamlit as st

# Dummy task list.
TASK_LIST = [
    {"task_id": 1, "description": "Task 1", "priority": "High", "status": "Completed"},
    {"task_id": 2, "description": "Task 2", "priority": "Medium", "status": "Active"},
    {"task_id": 3, "description": "Task 3", "priority": "Medium", "status": "Active"},
]


def add_task(task_description, task_priority):
    """Add a new task with provided description and priority."""
    feedback.write(f"Added task: {task_description} -- Priority: {task_priority}")


def complete_task(task_id):
    """Complete task with the provided task_id."""
    feedback.write(f"Completed task: {task_id}")


def delete_task(task_id):
    """Delete task with the provided task_id."""
    feedback.write(f"Deleted task: {task_id}")


# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# To Do list title element.
st.title("\N{MEMO} TO DO List")

# Divider line.
st.divider()

# Debug feedback container.
feedback = st.container()

# Create 3 column layout.
column_add, column_active, column_completed = st.columns(3, gap="large")

# Left column:
with column_add:

    # Header: New Task.
    st.header("New Task")

    # Form for adding tasks.
    with st.form(key="add_task_form", clear_on_submit=True):

        # Text input for description.
        description = st.text_input(label="Description")

        # Selectbox for priority (High, Medium, Low).
        priority = st.selectbox(
            label="Priority", options=["High", "Medium", "Low"], index=1
        )

        # Submit button labeled Add Task.
        submit = st.form_submit_button(label="Add Task")

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

                # Two columns with a 5 : 1 ratio.
                task_left, task_right = st.columns((5, 1))

                # Left column:
                with task_left:

                    # Subheader: task description.
                    st.subheader(task["description"])

                # Right column:
                with task_right:

                    # Complete task button.
                    st.button(
                        key=task["task_id"],
                        label=">>",
                        on_click=complete_task,
                        kwargs={"task_id": task["task_id"]},
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

                # Two columns with a 5 : 1 ratio.
                task_left, task_right = st.columns((5, 1))

                # Left column:
                with task_left:

                    # Subheader: task description.
                    st.subheader(task["description"])

                # Right column:
                with task_right:

                    # Delete task button.
                    st.button(
                        key=task["task_id"],
                        label="X",
                        on_click=delete_task,
                        kwargs={"task_id": task["task_id"]},
                    )
