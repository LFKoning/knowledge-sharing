"""Streamlit form demo."""

import streamlit as st


def add_user(name, age, role):
    """Print user details."""
    feedback.write(f"Added User:\n\n Name: {name}  --  Age: {age}  --  Role: {role}")


# Feedback container for add_user output.
feedback = st.container(border=True)


# Form for adding new users.
with st.form(key="form_add_user"):

    st.subheader("Add User")

    # Input fields for name, age and role.
    user_name = st.text_input(label="Name")
    user_age = st.text_input(label="Age")
    user_role = st.selectbox(label="Role", options=["Data Analist", "Data Engineer"])

    # Submit form button.
    submit = st.form_submit_button()

    # Handle form submission.
    if submit:

        if not user_name:
            st.error("Enter a name.")

        elif not user_age or not 0 < int(user_age) < 120:
            st.error("Enter a valid age.")

        else:
            add_user(user_name, user_age, user_role)
