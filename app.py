import streamlit as st
from directorypicker import st_directory_picker

my_selected_path = st_directory_picker()

st.markdown("---")
st.markdown(
    "You can access the selected path with the session state: `st.session_state.path`"
)
st.markdown(my_selected_path)
