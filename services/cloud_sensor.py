from typing import Any

import requests
import streamlit as st


@st.cache_data(ttl=30, show_spinner=False)
def get_latest_sensor_reading(
    supabase_url: str,
    api_key: str,
    device_id: str
) -> dict[str, Any]:

    supabase_url = supabase_url.rstrip("/")

    headers = {
        "apikey": str(api_key),
    }

    if str(api_key).startswith("eyJ"):
        headers["Authorization"] = f"Bearer {api_key}"

    response = requests.get(
        f"{supabase_url}/rest/v1/plant_readings",
        headers=headers,
        params={
            "select": "*",
            "device_id": f"eq.{device_id}",
            "order": "recorded_at.desc",
            "limit": "1",
        },
        timeout=20,
    )

    if not response.ok:
        raise RuntimeError(
            f"Supabase request failed: "
            f"{response.status_code} {response.text}"
        )

    rows = response.json()

    if not rows:
        raise RuntimeError(
            f"No readings for {device_id} have been uploaded yet."
        )

    return rows[0]


def get_logged_in_student_reading() -> dict[str, Any]:

    if not st.session_state.get("student_logged_in"):
        raise RuntimeError("Student is not signed in.")

    supabase_url = st.session_state.get("sensor_supabase_url")
    api_key = st.session_state.get("sensor_publishable_key")
    device_id = st.session_state.get("device_id")

    if not supabase_url:
        raise RuntimeError("Missing sensor Supabase URL.")

    if not api_key:
        raise RuntimeError("Missing sensor publishable key.")

    if not device_id:
        raise RuntimeError("Missing sensor device ID.")

    return get_latest_sensor_reading(
        supabase_url,
        api_key,
        device_id
    )
