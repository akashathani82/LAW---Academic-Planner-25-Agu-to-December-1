
import streamlit as st

# Load the HTML content from the file
with open("calendar.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Set Streamlit layout and render the calendar
st.set_page_config(layout="wide")
st.components.v1.html(html_content, height=800, scrolling=True)
