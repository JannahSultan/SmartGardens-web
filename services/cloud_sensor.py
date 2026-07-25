from typing import Any

import requests
import streamlit as st


def get_secret(name: str, default: str | None = None) -> str:
    try:
        value = st.secrets.get(name, default)
    except Exception:
        value = default

    if not value:
        raise RuntimeError(f"Missing Streamlit secret: {name}")

    return str(value)


@st.cache_data(ttl=30, show_spinner=False)
def get_latest_sensor_reading() -> dict[str, Any]:
    supabase_url = get_secret("SUPABASE_URL").rstrip("/")

    try:
        api_key = st.secrets.get("SUPABASE_PUBLISHABLE_KEY")
    except Exception:
        api_key = None

    if not api_key:
        try:
            api_key = st.secrets.get("SUPABASE_ANON_KEY")
        except Exception:
            api_key = None

    if not api_key:
        raise RuntimeError(
            "Missing SUPABASE_PUBLISHABLE_KEY or SUPABASE_ANON_KEY"
        )

    try:
        device_id = st.secrets.get("DEVICE_ID", "green-bean-1")
    except Exception:
        device_id = "green-bean-1"

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
            "No readings for green-bean-1 have been uploaded yet."
        )

    return rows[0]
