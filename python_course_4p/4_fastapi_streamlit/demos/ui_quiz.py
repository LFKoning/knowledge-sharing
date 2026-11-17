"""Streamlit counter demo."""

import random
import time

import streamlit as st

# Pick the winning a door.
correct_door = random.randint(1, 3)


def check_door(door_number):
    """Check if user picked the winning door."""
    if door_number == correct_door:
        feedback.markdown("### Hurrah YOU WON!")
    else:
        feedback.write(
            f"### Too bad, YOU LOST!\n\nThe correct door was: #{correct_door}."
        )
    time.sleep(2)


with st.container(horizontal_alignment="center"):
    # Quiz header.
    with st.container(width="content"):
        st.subheader("Can you guess the right door?!?")

    # Feedback container.
    with st.container(width="content"):
        feedback = st.empty()

st.divider()

# Create 3 columns for the buttons.
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
