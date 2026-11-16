"""Layout for the To Do list app in Streamlit."""

import streamlit as st


# Dummy task list.
TASK_LIST = [
    {"task_id": 1, "description": "Task 1", "priority": "High", "status": "Completed"},
    {"task_id": 2, "description": "Task 2", "priority": "Medium", "status": "Active"},
    {"task_id": 3, "description": "Task 3", "priority": "Medium", "status": "Active"},
]

# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# To Do list title element.
st.title("\N{memo} TO DO List")

# Divider line.
st.divider()

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

    # TODO: For loop for tasks in TASK_LIST.

        # TODO: Filter active tasks only.

            # Container with border for a task.
            with st.container(border=True):

                # Two columns with a 10 : 1 ratio.
                task_left, task_right = st.columns((10, 1))

                # Left column:
                with task_left:

                    # TODO: Change subheader to task description.

                # Right column:
                with task_right:

                    # Subheader: >>
                    st.subheader(">>")


# Right column:
with column_completed:

    # Header: Completed Tasks
    st.header("Completed Tasks")

    # TODO: Copy the for-loop from the center column.
    
    # TODO: Change the filter to display completed tasks.

    # TODO: Change the subheader >> into X.
