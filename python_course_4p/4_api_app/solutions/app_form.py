"""Layout for the To Do list app in Streamlit."""

import streamlit as st


def add_task(description, priority):
    """Add a new task with provided description and priority."""
    feedback.write(f"Added task: {description} -- Priority: {priority}")


# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# Add title element.
st.title("\N{MEMO} TO DO List")

# Divider line.
st.divider()

# Debug feedback container.
feedback = st.container()

# Create 3 column layout.
column_add, column_active, column_completed = st.columns(3, gap="large")

# Left column:
with column_add:

    # Header: Add Task.
    st.header("New Task")

    # Add your form here.
    with st.form("add_task_form", clear_on_submit=True):

        # Add a text input for description.
        description = st.text_input("Description")

        # Add a selectbox for priority (High, Medium, Low).
        priority = st.selectbox("Priority", options=["High", "Medium", "Low"], index=1)

        # Add a submit button labeled Add Task.
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

            # Create subheader: >>
            st.subheader(">>")


# Right column:
with column_completed:

    # Header: Completed Tasks
    st.header("Completed Tasks")
