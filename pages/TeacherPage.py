import streamlit as st
from supabase import create_client


# --------------------------------------------------
# CENTRAL SUPABASE CONNECTION
# --------------------------------------------------

central_supabase = create_client(
    st.secrets["CENTRAL_SUPABASE_URL"],
    st.secrets["CENTRAL_SUPABASE_PUBLISHABLE_KEY"]
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "teacher_logged_in" not in st.session_state:
    st.session_state.teacher_logged_in = False

if "teacher_id" not in st.session_state:
    st.session_state.teacher_id = None

if "teacher_email" not in st.session_state:
    st.session_state.teacher_email = None

if "teacher_access_token" not in st.session_state:
    st.session_state.teacher_access_token = None

if "teacher_refresh_token" not in st.session_state:
    st.session_state.teacher_refresh_token = None


# --------------------------------------------------
# LOGGED-IN TEACHER DASHBOARD
# --------------------------------------------------

if st.session_state.teacher_logged_in:

    st.title("Teacher Dashboard 🍎")

    st.write(
        f"Signed in as **{st.session_state.teacher_email}**"
    )

    st.success("Teacher login successful.")

    st.subheader("My Groups")

    st.info(
        "Your student groups will appear here once we add the group system."
    )

    if st.button("Log Out"):

        central_supabase.auth.sign_out()

        st.session_state.teacher_logged_in = False
        st.session_state.teacher_id = None
        st.session_state.teacher_email = None
        st.session_state.teacher_access_token = None
        st.session_state.teacher_refresh_token = None

        st.rerun()


# --------------------------------------------------
# TEACHER LOGIN / SIGN UP
# --------------------------------------------------

else:

    st.title("SmartGardens Teacher Portal 🍎")

    st.write(
        "Sign in or create a teacher account to manage your student groups."
    )

    sign_in_tab, create_account_tab = st.tabs(
        ["Sign In", "Create Account"]
    )


    # --------------------------------------------------
    # SIGN IN
    # --------------------------------------------------

    with sign_in_tab:

        st.subheader("Teacher Sign In")

        sign_in_email = st.text_input(
            "Email",
            key="teacher_sign_in_email"
        )

        sign_in_password = st.text_input(
            "Password",
            type="password",
            key="teacher_sign_in_password"
        )

        if st.button(
            "Sign In",
            key="teacher_sign_in_button"
        ):

            if not sign_in_email or not sign_in_password:

                st.error(
                    "Please enter both your email and password."
                )

            else:

                try:

                    response = central_supabase.auth.sign_in_with_password(
                        {
                            "email": sign_in_email,
                            "password": sign_in_password
                        }
                    )

                    if response.user and response.session:

                        st.session_state.teacher_logged_in = True

                        st.session_state.teacher_id = (
                            response.user.id
                        )

                        st.session_state.teacher_email = (
                            response.user.email
                        )

                        st.session_state.teacher_access_token = (
                            response.session.access_token
                        )

                        st.session_state.teacher_refresh_token = (
                            response.session.refresh_token
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Unable to sign in."
                        )

                except Exception as error:

                    st.error(
                        f"Sign in failed: {error}"
                    )


    # --------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------

    with create_account_tab:

        st.subheader("Create Teacher Account")

        new_email = st.text_input(
            "Email",
            key="teacher_create_email"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="teacher_create_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="teacher_confirm_password"
        )

        if st.button(
            "Create Account",
            key="teacher_create_account_button"
        ):

            if not new_email or not new_password:

                st.error(
                    "Please enter an email and password."
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                try:

                    response = central_supabase.auth.sign_up(
                        {
                            "email": new_email,
                            "password": new_password
                        }
                    )

                    if response.user:

                        st.success(
                            "Teacher account created successfully."
                        )

                    else:

                        st.error(
                            "Unable to create account."
                        )

                except Exception as error:

                    st.error(
                        f"Account creation failed: {error}"
                    )


# --------------------------------------------------
# BACK TO MAIN SITE
# --------------------------------------------------

st.divider()

if st.button(
    "Go back to the main SmartGardens page 🌱"
):
    st.switch_page("app.py")
