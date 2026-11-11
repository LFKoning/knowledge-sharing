import streamlit as st


# Set page title and layout.
st.set_page_config(page_title="Layout Demo", layout="wide")

# Create columns.
left_col, right_col = st.columns(2)

# Left column elements.
with left_col:
    st.header("Left Column")

    # L1 container.
    with st.container(border=True):
        st.subheader("L1 container")

    # L2 container.
    with st.container(border=True):
        st.subheader("L2 container")


# Right column elements.
with right_col:
    st.header("Right Column")

    # R2 container.
    with st.container(border=True):
        st.subheader("R1 container")
