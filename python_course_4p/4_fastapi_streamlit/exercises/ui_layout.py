"""Layout for the To Do list app in Streamlit."""

import streamlit as st

# Page configuration.
st.set_page_config(page_title="TO DO list", layout="wide")

# Add title element.

# Divider line.
st.divider()

# Create a 3 column layout.


# Left column:

    # Header: New Task.


# Center column:

    # Header: Active Tasks.

    # Add a container with border for a task.

        # Create 2 columns with ratio 5 : 1.

        # Left column:

            # Create subheader: Task 1

        # Right column:

            # Create subheader: >>


# Right column:

  # Header: Completed Tasks
