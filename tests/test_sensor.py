"""
test_sensor.py

Purpose:
Tests the PlantSensor class.
"""

import asyncio
from models.plant_sensor import PlantSensor

async def main():

    sensor = PlantSensor("BA1F2181-D768-8452-D384-8B305A23F7A8")

    readings = await sensor.get_readings()

    print("Current Plant Readings")
    print("----------------------")

    print(f"Temperature : {readings['temperature']} °C")
    print(f"Light       : {readings['light']} lux")
    print(f"Moisture    : {readings['moisture']} %")
    print(f"Fertility   : {readings['fertility']} µS/cm")


asyncio.run(main())