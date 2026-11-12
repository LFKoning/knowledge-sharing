"""Streamlit form demo."""

import streamlit as st


def add_user(user_name, user_age, user_role):
    """Print user details."""
    feedback.write(
        f"Added User:\n\n Name: {user_name}  --  Age: {user_age}  --  Role: {user_role}"
    )


st.subheader("Add User Form")
feedback = st.container(border=True)

with st.form(key="demo_form"):

    # Input fields for name, age and role.
    name = st.text_input(label="Name", key="input_name")
    age = st.text_input(label="Age", key="input_age")
    role = st.selectbox(label="Role", options=["Data Analist", "Data Engineer"])

    submit = st.form_submit_button()

    # Handle form submission.
    if submit:
        if not name:
            st.error("Enter a name.")
        elif not age or not 0 < int(age) < 120:
            st.error("Enter a valid age.")
        else:
            add_user(name, age, role)
