"""
test_plant_health.py

Purpose:
Combines the real sensor data with plant health rules.
"""

import asyncio
from models.plant_sensor import PlantSensor
from models.plant import Plant


async def main():
    sensor = PlantSensor("5C:85:7E:B0:98:C6")

    green_bean = Plant(
    name="Green Bean",
    ideal_temperature=(10, 35),
    ideal_light=(3800, 100000),
    ideal_moisture=(20, 65),
    ideal_fertility=(100, 2200)
    )

    readings = await sensor.get_readings()
    health_report = green_bean.check_health(readings)

    print("Current Readings")
    print("----------------")
    print(readings)

    print("\nGreen Bean Health Report")
    print("------------------------")
    print(health_report)


asyncio.run(main())