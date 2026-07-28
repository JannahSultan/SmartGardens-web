import streamlit as st

from game_data.game_state import initialize_game, reset_game

initialize_game()

st.title("The Sprout Lab 🔬")
st.write("Answer questions, solve mysteries, learn!")

if st.button("Go back to the main SmartGardens page 🌱"):
        st.switch_page("app.py")

with st.container(border=True):
    st.subheader("Question Bank")

    # Button to go to trivia
    if st.button("Go to Question Bank"):
        st.switch_page("pages/QuestionBank.py")

    # Reset game
    if st.button("Reset Game", key="resetQuestionBank"):
        reset_game()
        st.rerun()

    # Display game stats

    st.metric(
        "🧠 Questions Answered",
        f"{st.session_state.questions_answered}"
    )

    progress = st.session_state.questions_answered
    st.progress(progress)

    st.write(
        f"You have answered {st.session_state.questions_answered} out of 300 questions!"
    )

with st.container(border=True):
    st.subheader("Plant Mystery")

    if st.button("Go to Plant Mystery"):
        st.switch_page("pages/PlantMystery.py")

    if st.button("Reset Game", key="resetMystery"):
        reset_game()
        st.rerun()

    st.metric(
        "📊 Number of mysteries solved",
        st.session_state.mysteries_solved
    )

with st.container(border=True):

    st.subheader("Climate Challenge")

    st.write(
        "Manage your farm through droughts, heat waves, and changing weather!"
    )

    if st.button("Start Climate Challenge"):
        st.switch_page("pages/ClimateChallenge.py")

    if st.button("Reset Game", key="resetClimateChallenge"):
        reset_game()
        st.rerun()

    st.metric(
        "🌎 Climate Challenges Completed",
        st.session_state.climate_challenges_completed
    )
    
