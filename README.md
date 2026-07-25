# SmartGardens Plant Sensor Dashboard

SmartGardens is a plant-monitoring system that uses an HHCC Flower Care Bluetooth sensor, a Raspberry Pi Zero W, Supabase, and Streamlit.

The Raspberry Pi stays near the plant, reads the sensor through Bluetooth, and uploads the measurements to Supabase. The Streamlit website retrieves the newest reading from Supabase, analyses the plant’s health, and displays care advice.

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


