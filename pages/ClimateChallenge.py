import streamlit as st

from game_data.climate_scenarios import climate_scenarios
from game_data.game_state import initialize_game


initialize_game()


st.title("🌎 Climate Challenge")

st.write(
    "Manage your plants through changing climate conditions!"
)

if st.button("Go back to The Sprout Lab 🔬"):
        st.switch_page("pages/SproutLab.py")


# Pick scenario

if "climate_round" not in st.session_state:
    st.session_state.climate_round = 0


scenario = climate_scenarios[
    st.session_state.climate_round
]


with st.container(border=True):

    st.subheader(
        f"⚠️ Climate Event: {scenario['name']}"
    )

    st.write(
        f"🌱 Plant: {scenario['plant']}"
    )

    st.write(
        scenario["description"]
    )


    st.subheader("Current Conditions")

    for key, value in scenario["conditions"].items():
        st.write(
            f"**{key}:** {value}"
        )


st.divider()


st.subheader("Decision")


answer = st.radio(
    scenario["question"],
    scenario["options"]
)


if st.button("Submit Decision 🌱"):

    if answer == scenario["answer"]:

        st.success(
            "Great decision! Your plants are healthier 🌿"
        )

        st.session_state.correct_answers += 1


    else:

        st.error(
            f"Better choice: {scenario['answer']}"
        )


    st.session_state.climate_challenges_completed += 1


    # Move to next scenario

    if (
        st.session_state.climate_round + 1
        < len(climate_scenarios)
    ):

        st.session_state.climate_round += 1

    else:

        st.success(
            "🎉 You completed the climate simulation!"
        )

        st.session_state.climate_round = 0


    st.rerun()
