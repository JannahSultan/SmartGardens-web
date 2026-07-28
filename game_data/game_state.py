import streamlit as st


def initialize_game():

    if "questions_answered" not in st.session_state:
        st.session_state.questions_answered = 0

    if "correct_answers" not in st.session_state:
        st.session_state.correct_answers = 0

    if "mysteries_solved" not in st.session_state:
        st.session_state.mysteries_solved = 0

    if "mystery_unlocked" not in st.session_state:
        st.session_state.mystery_unlocked = 0

    if "climate_challenges_completed" not in st.session_state:
        st.session_state.climate_challenges_completed = 0



def reset_game():

    st.session_state.questions_answered = 0
    st.session_state.correct_answers = 0
    st.session_state.mysteries_solved = 0
    st.session_state.mystery_unlocked = 0
    st.session_state.climate_challenges_completed = 0
