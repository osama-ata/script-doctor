import streamlit as st
from script_doctor import (
    read_docx_table,  # Changed from read_docx_files_in_directory
)

st.set_page_config(page_title="Script Doctor")
st.title("🩺 Script Doctor")
st.write("This is your Streamlit app inside a structured Python project.")

# UI
uploaded_files = st.file_uploader(
    "Select files", type=["docx"], accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"File: {uploaded_file.name}")
        # Process docx files
        if uploaded_file.name.endswith(".docx"):
            # python-docx Document() can take a file-like object.
            # We'll adapt read_docx_table to accept it.
            with st.expander("Expand to view table", expanded=False):
                table = read_docx_table(uploaded_file)  # Pass the file-like object
                if table:
                    st.table(table)
                else:
                    st.write("No table found in .docx file.")
        elif uploaded_file.name.endswith(".doc"):
            st.write("Processing for .doc files is not yet implemented.")
        else:
            st.write("Unsupported file type.")
