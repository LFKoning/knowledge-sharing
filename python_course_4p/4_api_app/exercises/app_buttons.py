"""Layout for the To Do list app in Streamlit."""

import streamlit as st


# Dummy task list.
TASK_LIST = [
    {"task_id": 1, "description": "Task 1", "priority": "High", "status": "Completed"},
    {"task_id": 2, "description": "Task 2", "priority": "Medium", "status": "Active"},
    {"task_id": 3, "description": "Task 3", "priority": "Medium", "status": "Active"},
]


def complete_task(task_id):
    """Complete task with the provided task_id."""
    feedback.write(f"Completed task: {task_id}")


def delete_task(task_id):
    """Delete task with the provided task_id."""
    feedback.write(f"Deleted task: {task_id}")


# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# To Do list title element.
st.title("\N{memo} TO DO List")

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

                    # TODO: Add a complete task button.
                    # - Set label to >>.
                    # - Set key to the task's task_id.
                    # - Call the complete_task function on click.
                    # - Provide the task_id as an argument.


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

                    # TODO: Add a delete task button.
                    # - Set label to X.
                    # - Set key to the task's task_id.
                    # - Call the delete_task function on click.
                    # - Provide the task_id as an argument.
