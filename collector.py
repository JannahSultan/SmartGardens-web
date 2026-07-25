import asyncio
import logging
import os
from typing import Any

import requests

from models.plant_sensor import PlantSensor


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_SECRET_KEY = os.environ["SUPABASE_SECRET_KEY"]
SENSOR_MAC = os.environ.get("SENSOR_MAC", "5C:85:7E:B0:98:C6")
DEVICE_ID = os.environ.get("DEVICE_ID", "green-bean-1")
READ_INTERVAL_SECONDS = int(
    os.environ.get("READ_INTERVAL_SECONDS", "300")
)


def get_value(readings: Any, *possible_names: str):
    """
    Read a value whether readings is a dictionary
    or an object containing attributes.
    """
    if isinstance(readings, dict):
        for name in possible_names:
            if name in readings:
                return readings[name]
        return None

    for name in possible_names:
        if hasattr(readings, name):
            return getattr(readings, name)

    return None


def upload_reading(payload: dict) -> None:
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/plant_readings",
        headers={
            "apikey": SUPABASE_SECRET_KEY,
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
        json=payload,
        timeout=30,
    )

    if not response.ok:
        raise RuntimeError(
            f"Supabase upload failed: "
            f"{response.status_code} {response.text}"
        )


async def main() -> None:
    sensor = PlantSensor(SENSOR_MAC)

    logging.info("Plant sensor collector started")
    logging.info("Sensor address: %s", SENSOR_MAC)

    while True:
        try:
            readings = await sensor.get_readings()

            logging.info("Raw sensor reading: %s", readings)

            payload = {
                "device_id": DEVICE_ID,
                "temperature_c": get_value(
                    readings,
                    "temperature",
                    "temperature_c",
                ),
                "light_lux": get_value(
                    readings,
                    "light",
                    "light_lux",
                    "illuminance",
                ),
                "moisture_percent": get_value(
                    readings,
                    "moisture",
                    "moisture_percent",
                ),
                "fertility_us_cm": get_value(
                    readings,
                    "fertility",
                    "conductivity",
                    "fertility_us_cm",
                ),
                "battery_percent": get_value(
                    readings,
                    "battery",
                    "battery_percent",
                ),
                "error": None,
            }

            await asyncio.to_thread(upload_reading, payload)
            logging.info("Reading uploaded successfully: %s", payload)

        except Exception as error:
            logging.exception("Reading failed: %s", error)

        await asyncio.sleep(READ_INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(main())
