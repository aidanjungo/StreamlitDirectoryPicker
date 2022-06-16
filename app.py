import streamlit as st
from directorypicker import st_directory_picker

my_selected_path = st_directory_picker()

st.markdown("---")
st.markdown(my_selected_path)
