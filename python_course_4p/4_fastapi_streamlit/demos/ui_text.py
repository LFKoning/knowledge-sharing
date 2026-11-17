import streamlit as st


# Set page title and layout.
st.set_page_config(page_title="Hello World!", layout="wide")

# Create a text header.
st.title("This is a title")

# And a header
st.header("This is a header")

# And a subheader.
st.subheader("This is a subheader")

# Normal text.
st.write("This is normal text using write")

# Markdown.
st.write("This is **markdown**")
