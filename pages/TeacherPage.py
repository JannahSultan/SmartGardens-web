import streamlit as st

st.title("Teacher Dashboard 🍎")
st.write("Click below to view information about the student data and group progress.")

if st.button("Go back to the main SmartGardens page 🌱"):
    st.switch_page("app.py")


# Function to create group cards
def group_card(title, color, members, plant, questions, mysteries, challenges):

    st.markdown(
        f"""
        <div style="
            background-color: {color};
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #000000;
            margin-bottom: 15px;
        ">
            <h3>{title}</h3>
            <p><b>Group Members:</b> {members}</p>
            <p><b>Assigned Plant:</b> {plant}</p>
            <p><b>Question Bank:</b> {questions}</p>
            <p><b>Plant Mystery:</b> {mysteries}</p>
            <p><b>Climate Challenge:</b> {challenges}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -------------------------
# Group 1
# -------------------------

group_card(
    "🌱 Group #1",
    "#E8F5E9",
    "Emma Rodriguez, Liam Chen, Olivia Patel, Noah Williams, Sophia Nguyen",
    "Green Bean Plant #1",
    "52/300 Questions Answered",
    "1/6 Mysteries Solved",
    "4/10 Challenges Done"
)


# -------------------------
# Group 2
# -------------------------

group_card(
    "🌱 Group #2",
    "#FFF9C4",
    "Ethan Johnson, Ava Martinez, Lucas Kim, Mia Thompson, Jackson Lee",
    "Tomato Plant #1",
    "295/300 Questions Answered",
    "2/6 Mysteries Solved",
    "1/10 Challenges Done"
)


# -------------------------
# Group 3
# -------------------------

group_card(
    "🌱 Group #3",
    "#FFCDD2",
    "Isabella Garcia, Aiden Smith, Chloe Brown, Mason Wilson",
    "Green Bean Plant #2",
    "14/300 Questions Answered",
    "1/6 Mysteries Solved",
    "0/10 Challenges Done"
)


# -------------------------
# Group 4
# -------------------------

group_card(
    "🌱 Group #4",
    "#FFF9C4",
    "Lily Anderson, Benjamin Davis, Zoe Taylor, Henry Clark",
    "Radish Plant #1",
    "288/300 Questions Answered",
    "1/6 Mysteries Solved",
    "2/10 Challenges Done"
)


# -------------------------
# Group 5
# -------------------------

group_card(
    "🌱 Group #5",
    "#C8E6C9",
    "Grace Thomas, Daniel White, Hannah Moore, Caleb Martin, Aria Scott, Jack Miller",
    "Tomato Plant #2",
    "134/300 Questions Answered",
    "5/6 Mysteries Solved",
    "10/10 Challenges Done"
)
