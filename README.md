# SmartGardens Plant Sensor Dashboard

SmartGardens is a plant-monitoring system that uses an HHCC Flower Care Bluetooth sensor, a Raspberry Pi Zero W, Supabase, and Streamlit.

The Raspberry Pi stays near the plant, reads the sensor through Bluetooth, and uploads the measurements to Supabase. The Streamlit website retrieves the newest reading from Supabase, analyses the plant’s health, and displays care advice.

The device viewing the website does not need to be connected to Bluetooth or to the same Wi-Fi network as the Raspberry Pi.

## Features
Displays temperature, soil moisture, light, fertility, and battery level
Supports different green bean growth stages
Compares current readings with ideal plant conditions
Calculates an overall plant health score
Displays plant status and mood
Generates care advice when conditions are too low or too high
Retrieves readings from Supabase
Can be accessed from anywhere with an internet connection
## Technologies Used
Python
Streamlit
Supabase
Raspberry Pi Zero W
Bluetooth Low Energy
HHCC Flower Care sensor
GitHub
Requests
## Project Structure

SmartGardens-web/

│

├── app.py

├── main.py

├── requirements.txt

│

├── models/

│   ├── __init__.py

│   ├── plant.py

│   ├── plant_mood.py

│   ├── plant_profiles.py

│   └── plant_status.py

│

├── services/

│   ├── __init__.py

│   ├── cloud_sensor.py

│   └── plant_advice.py

│

└── data/

    └── plant_settings.json
    

## Website Setup

Install the required packages:

pip install -r requirements.txt

Run the Streamlit app locally:

streamlit run app.py
Streamlit Secrets

The app requires the following secrets:

SUPABASE_URL = "YOUR_SUPABASE_PROJECT_URL"
SUPABASE_PUBLISHABLE_KEY = "YOUR_SUPABASE_PUBLISHABLE_KEY"
DEVICE_ID = "green-bean-1"

For local development, place them in:

.streamlit/secrets.toml

For Streamlit Community Cloud, add them through the app’s Secrets settings.

Do not commit secrets.toml, Supabase secret keys, Raspberry Pi passwords, or Wi-Fi passwords to GitHub.

## Raspberry Pi Collector

The Raspberry Pi runs a separate collector program that:

Connects to the HHCC Flower Care sensor through Bluetooth.
Reads the current plant measurements.
Uploads the readings to Supabase.
Repeats automatically at a set interval.

The collector and Bluetooth-specific files are intentionally not included in this website repository.

## Supabase Table

The website expects a Supabase table named:

plant_readings

The table contains fields for:

device_id
recorded_at
temperature_c
light_lux
moisture_percent
fertility_us_cm
battery_percent
error
## Deployment

The website is deployed using Streamlit Community Cloud.

The Raspberry Pi does not host the website. It acts as a gateway between the Bluetooth sensor and the Supabase database.

## Security

The website uses a Supabase publishable key.

The Raspberry Pi uses a separate private Supabase secret key for uploading data. That secret key must never be placed in this repository or exposed in the Streamlit website.

## Current Plant

The current version is configured for a green bean plant and supports different green bean growth stages.

## Future Improvements

Possible future additions include:

Support for more plant types
Historical graphs
Notifications when readings become unhealthy
Multiple sensors and plants
User accounts
Improved mobile layout
Automatic growth-stage recommendations

## System Architecture

```text
HHCC Flower Care Sensor
        ↓ Bluetooth
Raspberry Pi Zero W
        ↓ Internet
Supabase Database
        ↓ Internet
Streamlit Website
        ↓
Phone or Computer


