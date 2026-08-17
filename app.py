"""
app.py

Main Streamlit interface for the SmartGardens project.
"""

import json
from pathlib import Path

import streamlit as st

from main import get_green_bean_report
from models.plant_profiles import GREEN_BEAN_STAGES
from services.cloud_sensor import get_logged_in_student_reading

PROJECT_FOLDER = Path(__file__).resolve().parent
DATA_FOLDER = PROJECT_FOLDER / "data"
SETTINGS_FILE = DATA_FOLDER / "plant_settings.json"


def load_saved_stage():
    """
    Load the previously selected growth stage.
    """

    if not SETTINGS_FILE.exists():
        return None

    try:
        with SETTINGS_FILE.open(
            "r",
            encoding="utf-8",
        ) as file:
            settings = json.load(file)

        stage = settings.get("green_bean_stage")

        if stage in GREEN_BEAN_STAGES:
            return stage

    except (OSError, json.JSONDecodeError):
        return None

    return None


def save_stage(stage):
    DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True,
    )

    settings = {
        "green_bean_stage": stage,
    }

    with SETTINGS_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            settings,
            file,
            indent=4,
        )
        
def display_stage_selector():
    """
    Ask the user to select the plant's growth stage.
    """

    st.subheader("Choose Your Plant Stage")

    selected_stage = st.selectbox(
        "Which stage is your green bean plant currently in?",
        options=list(GREEN_BEAN_STAGES.keys()),
        index=None,
        placeholder="Choose a growth stage",
        format_func=lambda stage: stage.title(),
    )

    save_button = st.button(
        "Save Growth Stage",
        type="primary",
        disabled=selected_stage is None,
    )

    if save_button:
        save_stage(selected_stage)

        st.session_state.green_bean_stage = selected_stage
        st.session_state.pop("plant_report", None)

        st.rerun()


def display_ideal_conditions(ideals):
    """
    Display the ideal conditions for the selected stage.
    """

    st.subheader("Ideal Conditions")

    left_column, right_column = st.columns(2)

    with left_column:
        st.write(
            f"**Temperature:** "
            f"{ideals['temperature'][0]}–"
            f"{ideals['temperature'][1]} °C"
        )

        st.write(
            f"**Soil moisture:** "
            f"{ideals['moisture'][0]}–"
            f"{ideals['moisture'][1]}%"
        )

    with right_column:
        st.write(
            f"**Light:** "
            f"{ideals['light'][0]:,}–"
            f"{ideals['light'][1]:,} lux"
        )

        st.write(
            f"**Fertility:** "
            f"{ideals['fertility'][0]}–"
            f"{ideals['fertility'][1]} µS/cm"
        )


def display_sensor_readings(readings):
    """
    Display readings returned by the Flower Care sensor.
    """

    st.subheader("Current Sensor Readings")

    columns = st.columns(5)

    sensor_values = [
        (
            "Temperature",
            readings.get("temperature"),
            "°C",
        ),
        (
            "Moisture",
            readings.get("moisture"),
            "%",
        ),
        (
            "Fertility",
            readings.get("fertility"),
            "µS/cm",
        ),
        (
            "Light",
            readings.get("light"),
            "lux",
        ),
        (
            "Battery",
            readings.get("battery"),
            "%",
        ),
    ]

    for column, sensor_value in zip(
        columns,
        sensor_values,
    ):
        label, value, unit = sensor_value

        with column:
            if value is None:
                st.metric(
                    label,
                    "Unavailable",
                )
            else:
                st.metric(
                    label,
                    f"{value} {unit}",
                )


def display_health_report(health_report):
    """
    Display whether every measurement is good, low, or high.
    """

    st.subheader("Health Analysis")

    for category, result in health_report.items():
        readable_category = category.replace(
            "_",
            " ",
        ).title()

        message = f"{readable_category}: {result}"

        if result == "Good":
            st.success(message)

        elif result == "Too Low":
            st.warning(message)

        else:
            st.error(message)


def display_report(report):
    """
    Display the complete plant report.
    """

    st.header(
        f"{report['plant_name']} — "
        f"{report['stage'].title()} Stage"
    )

    status_column, score_column, mood_column = st.columns(3)

    with status_column:
        st.metric(
            "Overall Status",
            report["status"],
        )

    with score_column:
        st.metric(
            "Health Score",
            f"{report['score']}/100",
        )

    with mood_column:
        st.metric(
            "Plant Mood",
            report["mood"],
        )

    display_ideal_conditions(
        report["ideals"]
    )

    display_sensor_readings(
        report["readings"]
    )

    display_health_report(
        report["health_report"]
    )

    st.subheader("Care Advice")

    if report["advice"]:
        for advice_item in report["advice"]:
            st.info(advice_item)

    else:
        st.success(
            "All checked conditions are currently healthy."
        )


def main():
    """
    Start the Streamlit application.
    """

    st.set_page_config(
        page_title="PlantPal",
        page_icon="🌱",
        layout="wide",
    )

    if not st.session_state.get("student_logged_in"):
        st.title("🌱 SmartGardens")

        st.warning(
            "Please sign in with your group's username and password."
        )

        if st.button("Go to Student Sign In"):
            st.switch_page("pages/StudentPage.py")

        st.stop()

    st.title("🌱 PlantPal")

    st.write(
        "Monitor your green bean plant using your "
        "Flower Care 4-in-1 sensor."
    )

    if "green_bean_stage" not in st.session_state:
        st.session_state.green_bean_stage = load_saved_stage()

    stage = st.session_state.green_bean_stage

    if stage is None:
        display_stage_selector()
        st.stop()
        
    with st.container(border=True):
        if st.button("Go to The Sprout Lab 🔬"):
            st.switch_page("pages/SproutLab.py")

        st.write("The place to go to answer questions, solve plant mysteries, and learn!")

    with st.container(border=True):
        if st.button("Go to the Teacher Dashboard 🍎"):
            st.switch_page("pages/TeacherPage.py")

        st.write("Use this page to access student data, progress, and group information!")


    st.caption(
        f"Saved growth stage: **{stage.title()}**"
    )

    button_column1, button_column2 = st.columns(2)

    with button_column1:
        change_stage_button = st.button(
            "Change Growth Stage"
        )

    with button_column2:
        read_sensor_button = st.button(
            "Read Plant Sensor",
            type="primary",
        )

    if change_stage_button:
        st.session_state.green_bean_stage = None
        st.session_state.pop("plant_report", None)
        st.rerun()

    if read_sensor_button:
        with st.spinner(
            "Loading the latest reading from Supabase..."
        ):
            try:
                latest_reading = get_logged_in_student_reading()

                readings = {
                    "temperature": latest_reading.get(
                        "temperature_c"
                    ),
                    "light": latest_reading.get(
                        "light_lux"
                    ),
                    "moisture": latest_reading.get(
                        "moisture_percent"
                    ),
                    "fertility": latest_reading.get(
                        "fertility_us_cm"
                    ),
                    "battery": latest_reading.get(
                        "battery_percent"
                    ),
                }

                report = get_green_bean_report(
                    stage,
                    readings,
                )

                st.session_state["plant_report"] = report
                st.rerun()

            except Exception as error:
                st.error(
                    "The button worked, but the plant data "
                    "could not be loaded."
                )
                st.exception(error)

    if "plant_report" in st.session_state:
        display_report(
            st.session_state.plant_report
        )

    else:
        display_ideal_conditions(
            GREEN_BEAN_STAGES[stage]
        )

        st.info(
            "Press “Read Plant Sensor” to get the "
            "plant's current measurements."
        )


if __name__ == "__main__":
    main()
