import streamlit as st

from game_data.mysteries import mysteries
from game_data.game_state import initialize_game


initialize_game()


# -------------------------
# Initialize Mystery States
# -------------------------

if "current_mystery" not in st.session_state:
    st.session_state.current_mystery = None

if "mystery_question" not in st.session_state:
    st.session_state.mystery_question = 0

if "mystery_correct_answers" not in st.session_state:
    st.session_state.mystery_correct_answers = 0

if "mystery_feedback" not in st.session_state:
    st.session_state.mystery_feedback = ""

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

if "mystery_completed" not in st.session_state:
    st.session_state.mystery_completed = False

if "mystery_failed" not in st.session_state:
    st.session_state.mystery_failed = False



# -------------------------
# Page Setup
# -------------------------

st.title("🌱 Plant Mystery Lab")

st.write(
    "Solve plant cases by analyzing sensor readings and clues!"
)


if st.button("Go back to The Sprout Lab 🔬"):
    st.switch_page("pages/SproutLab.py")



# -------------------------
# Mystery Selection Screen
# -------------------------

if st.session_state.current_mystery is None:

    st.subheader("Choose a Mystery")


    # Failed mystery message
    if st.session_state.mystery_failed:

        st.error(
            st.session_state.mystery_feedback
        )

        if st.button("Try Again"):

            st.session_state.mystery_failed = False
            st.session_state.mystery_feedback = ""

            st.rerun()



    for index, mystery in enumerate(mysteries):

        mystery_number = index + 1


        with st.container(border=True):

            if mystery_number <= st.session_state.mystery_unlocked + 1:


                st.write(
                    f" Mystery #{mystery_number}: {mystery['name']}"
                )


                if st.button(
                    f"Start Mystery #{mystery_number}",
                    key=f"mystery_{index}"
                ):

                    st.session_state.current_mystery = index
                    st.session_state.mystery_question = 0
                    st.session_state.mystery_correct_answers = 0
                    st.session_state.mystery_feedback = ""
                    st.session_state.answer_submitted = False
                    st.session_state.mystery_completed = False
                    st.session_state.mystery_failed = False

                    st.rerun()


            else:

                st.write(
                    f"🔒 Mystery #{mystery_number}: Locked"
                )




# -------------------------
# Mystery Gameplay
# -------------------------

else:

    mystery = mysteries[
        st.session_state.current_mystery
    ]


    st.divider()


    st.subheader(
        f"🔎 {mystery['name']}"
    )


    # Case information
    with st.container(border=True):

        st.write(
            f"**Appearance:** {mystery['appearance']}"
        )


        st.subheader("Sensor Readings")


        for reading, value in mystery["readings"].items():

            st.write(
                f"**{reading}:** {value}"
            )



    # Mystery solved screen
    if st.session_state.mystery_completed:


        st.success(
            "🎉 Mystery Solved! You answered every question correctly!"
        )


        if st.button("Back to Mystery Selection 🌱"):

            st.session_state.current_mystery = None
            st.session_state.mystery_question = 0
            st.session_state.mystery_correct_answers = 0
            st.session_state.mystery_completed = False

            st.rerun()



    else:


        question_number = st.session_state.mystery_question

        question = mystery["questions"][question_number]


        st.subheader(
            f"Question {question_number + 1}/{len(mystery['questions'])}"
        )


        answer = st.radio(
            question["question"],
            question["options"],
            disabled=st.session_state.answer_submitted
        )



        # Submit Answer
        if not st.session_state.answer_submitted:


            if st.button("Submit Answer"):


                st.session_state.answer_submitted = True


                if answer == question["answer"]:

                    st.session_state.mystery_feedback = (
                        "✅ Correct!"
                    )

                    st.session_state.mystery_correct_answers += 1


                else:

                    st.session_state.mystery_feedback = (
                        f"❌ Incorrect! The correct answer was: "
                        f"{question['answer']}"
                    )


                st.rerun()



        # Show feedback
        if st.session_state.answer_submitted:


            st.write(
                st.session_state.mystery_feedback
            )


            if st.button("Next Question ➡️"):


                st.session_state.answer_submitted = False
                st.session_state.mystery_feedback = ""



                # More questions remain
                if question_number + 1 < len(mystery["questions"]):

                    st.session_state.mystery_question += 1



                # Finished all questions
                else:


                    total_questions = len(mystery["questions"])


                    # Perfect score
                    if (
                        st.session_state.mystery_correct_answers
                        == total_questions
                    ):


                        st.session_state.mysteries_solved += 1


                        # Unlock next mystery
                        if (
                            st.session_state.mystery_unlocked
                            <= st.session_state.current_mystery
                        ):

                            st.session_state.mystery_unlocked += 1


                        st.session_state.mystery_completed = True



                    # Failed
                    else:


                        wrong_answers = (
                            total_questions
                            - st.session_state.mystery_correct_answers
                        )


                        st.session_state.mystery_feedback = (
                            f"❌ Mystery Failed! You got "
                            f"{wrong_answers}/6 questions wrong. "
                            "Go back to the selection menu and try again!"
                        )


                        st.session_state.mystery_failed = True


                        st.session_state.current_mystery = None
                        st.session_state.mystery_question = 0
                        st.session_state.mystery_correct_answers = 0



                st.rerun()
