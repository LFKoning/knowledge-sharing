"""Streamlit counter demo."""

import random

import streamlit as st


# Picking a door
correct_door = random.randint(1, 3)


def check_door(door_number):
    """Check the winning door."""
    feedback.empty()
    if door_number == correct_door:
        feedback.markdown("### Hurrah YOU WON!")
    else:
        feedback.write(
            f"### Too bad, YOU LOST!\n\nThe correct door was {correct_door}."
        )


st.subheader("Quiz: Can you pick the right door?!?")
st.divider()

# Display output.
with st.container(horizontal_alignment="center"):
    feedback = st.container(width="content")
    feedback.write("Pick a door below...")

st.divider()

left, center, right = st.columns(3)

with left:
    st.button(
        key="door_1_button",
        label="Door #1",
        on_click=check_door,
        kwargs={"door_number": 1},
    )

with center:
    with st.container(horizontal_alignment="center"):

        st.button(
            key="door_2_button",
            label="Door #2",
            on_click=check_door,
            kwargs={"door_number": 2},
        )

with right:
    with st.container(horizontal_alignment="right"):
        st.button(
            key="door_3_button",
            label="Door #3",
            on_click=check_door,
            kwargs={"door_number": 3},
        )
