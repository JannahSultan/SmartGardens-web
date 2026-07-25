import asyncio
from models.plant_sensor import PlantSensor
from models.plant import Plant
from services.plant_advice import generate_advice
from models.plant_status import calculate_status
from models.plant_mood import get_plant_mood


async def main():

    # Create a PlantSensor object using our sensor's Bluetooth address.
    sensor = PlantSensor("5C:85:7E:B0:98:C6")

    # Create a Green Bean plant object with its ideal growing ranges.
    green_bean = Plant(
    name="Green Bean",
    ideal_temperature=(10, 35),
    ideal_light=(3800, 100000),
    ideal_moisture=(20, 65),
    ideal_fertility=(100, 2200)
    )

    # Get the current sensor readings.
    readings = await sensor.get_readings()

    # Compare the readings to the plant's ideal ranges.
    health_report = green_bean.check_health(readings)

    # Generate advice for the user.
    advice = generate_advice(health_report)

    # Calculate the overall health status and score.
    status, score = calculate_status(health_report)

    # NEW: Determine the plant's mood based on its score.
    mood = get_plant_mood(score)

    # Display the results.
    print("Green Bean Plant")
    print("----------------")
    print(f"Overall Status: {status}")
    print(f"Health Score: {score}/100")
    print(f"Plant Mood: {mood}")   # NEW

    print("\nReadings:")
    for key, value in readings.items():
        print(f"{key}: {value}")

    print("\nHealth:")
    for key, value in health_report.items():
        print(f"{key}: {value}")

    print("\nAdvice:")
    for item in advice:
        print("-", item)


asyncio.run(main())