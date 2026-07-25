import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* -----------------------------
       Entire App
    ------------------------------ */

    .stApp{
        background-color:#F8FBF4;
    }

    /* -----------------------------
       Section Cards
    ------------------------------ */

    .card{
        background:white;
        border:2px solid #A9D18E;
        border-radius:20px;
        padding:25px;
        margin-top:20px;
        margin-bottom:20px;

        box-shadow:
            0px 4px 10px rgba(0,0,0,0.08);
    }

    /* -----------------------------
       Section Titles
    ------------------------------ */

    .section-title{
        font-size:28px;
        font-weight:bold;
        color:#2E7D32;

        margin-bottom:15px;
    }

    /* -----------------------------
       Rounded Buttons
    ------------------------------ */

    .stButton>button{

        border-radius:15px;

        background:#2E7D32;

        color:white;

        border:none;

        padding:12px 25px;

        font-size:18px;

        font-weight:bold;
    }

    .stButton>button:hover{

        background:#3E9142;

    }

    </style>
    """, unsafe_allow_html=True)