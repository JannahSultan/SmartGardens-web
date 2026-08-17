import streamlit as st
import bcrypt
from supabase import create_client


central_admin = create_client(
    st.secrets["CENTRAL_SUPABASE_URL"],
    st.secrets["CENTRAL_SUPABASE_SECRET_KEY"]
)


if "student_logged_in" not in st.session_state:
    st.session_state.student_logged_in = False


if not st.session_state.student_logged_in:

    st.title("Student Sign In 🌱")

    username = st.text_input("Group Username")
    password = st.text_input(
        "Group Password",
        type="password"
    )

    if st.button("Sign In"):

        if not username or not password:
            st.error("Enter your username and password.")

        else:
            try:
                response = (
                    central_admin
                    .table("student_groups")
                    .select("*")
                    .eq("student_username", username)
                    .limit(1)
                    .execute()
                )

                if not response.data:
                    st.error("Incorrect username or password.")

                else:
                    group = response.data[0]

                    password_correct = bcrypt.checkpw(
                        password.encode("utf-8"),
                        group["student_password_hash"].encode("utf-8")
                    )

                    if not password_correct:
                        st.error("Incorrect username or password.")

                    else:
                        st.session_state.student_logged_in = True

                        st.session_state.student_group_id = group["id"]
                        st.session_state.student_group_name = group["group_name"]
                        st.session_state.student_group_plant_type = group.get("plant_type")
                        st.session_state.student_group_plant_stage = group.get("plant_stage")

                        st.session_state.sensor_supabase_url = (
                            group["supabase_url"]
                        )

                        st.session_state.sensor_publishable_key = (
                            group["supabase_publishable_key"]
                        )

                        st.session_state.device_id = (
                            group["device_id"]
                        )

                        st.switch_page("app.py")

            except Exception as error:
                st.error(f"Sign in failed: {error}")

else:

    st.success(
        f"Signed in as {st.session_state.student_group_name}"
    )

    if st.button("Go to Garden"):
        st.switch_page("app.py")

    if st.button("Log Out"):
        st.session_state.clear()
        st.rerun()
