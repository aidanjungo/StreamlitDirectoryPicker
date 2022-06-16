import streamlit as st
from pathlib import Path


def st_directory_picker(initial_path=Path()):

    st.markdown("#### Directory picker")

    if "path" not in st.session_state:
        st.session_state.path = initial_path.absolute()

    col1, col2, col3, col4 = st.columns([7, 1, 3, 1])

    with col1:
        st.markdown("#")
        st.markdown("..." + str(st.session_state.path)[-42:])

    with col2:
        st.markdown("#")
        if st.button("⬅️") and "path" in st.session_state:
            st.session_state.path = st.session_state.path.parent
            st.experimental_rerun()

    with col3:
        sub_directroies = [
            f.stem for f in st.session_state.path.iterdir() if f.is_dir()
        ]
        if sub_directroies:
            st.session_state.new_dir = st.selectbox("", sub_directroies)
        else:
            st.markdown("#")
            st.markdown(
                "<font color='#FF0000'>No subdir</font>", unsafe_allow_html=True
            )

    with col4:
        if sub_directroies:
            st.markdown("#")
            if st.button("➡️") and "path" in st.session_state:
                st.session_state.path = Path(
                    st.session_state.path, st.session_state.new_dir
                )
                st.experimental_rerun()

    st.markdown(f"**Selected directory:** {st.session_state.path}")

    return st.session_state.path
