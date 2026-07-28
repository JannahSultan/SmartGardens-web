import streamlit as st
import random

from game_data.questions import questions
from game_data.game_state import initialize_game

initialize_game()

st.title("🌱 Question Bank")

if st.button("Go back to The Sprout Lab 🔬"):
    st.switch_page("pages/SproutLab.py")

st.write(f"{st.session_state.questions_answered}/300 questions completed")

# Pick a question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

q = st.session_state.current_question

st.write(q["question"])

answer = st.radio(
    "Choose your answer:",
    q["answers"]
)

if st.button("Submit"):

    if answer == q["correct"]:
        st.session_state.correct_answers += 1
        st.session_state.feedback = "✅ Correct!"
        
    else:
        st.session_state.feedback = f"❌ Not quite! The correct answer was: {q['correct']}"

    st.session_state.questions_answered += 1


# Display feedback
if st.session_state.feedback:
    st.write(st.session_state.feedback)

    if st.button("Next Question"):
        st.session_state.current_question = random.choice(questions)
        st.session_state.feedback = ""
        st.rerun()
