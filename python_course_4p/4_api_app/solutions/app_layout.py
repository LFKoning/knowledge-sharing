"""Layout for the To Do list app in Streamlit."""

import streamlit as st

# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# Add title element.
st.title("\N{memo} TO DO List")

# Divider line.
st.divider()

# Create 3 column layout.
column_add, column_active, column_completed = st.columns(3, gap="large")

# Left column:
with column_add:

    # Header: Add Task.
    st.header("New Task")

# Center column:
with column_active:

    # Header: Active Tasks.
    st.header("Active Tasks")

    # Add a container with border for a task.
    with st.container(border=True):

        # Create 2 columns with ratio 10 : 1.
        task_left, task_right = st.columns((10, 1))

        # Left column:
        with task_left:

            # Create subheader: Task 1
            st.subheader("Task 1")

        # Right column:
        with task_right:

            # Create subheader: [X]
            st.subheader(">>")


# Right column:
with column_completed:

    # Header: Completed Tasks
    st.header("Completed Tasks")
