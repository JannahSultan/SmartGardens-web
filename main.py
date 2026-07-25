"""
main.py

Combines the sensor, plant profile, health analysis,
status, mood, and care advice.
"""

import asyncio

from models.plant import Plant
from models.plant_profiles import get_green_bean_ideals
from models.plant_status import calculate_status
from models.plant_mood import get_plant_mood
from services.plant_advice import generate_advice


SENSOR_ADDRESS = "5C:85:7E:B0:98:C6"


def get_green_bean_report(stage, readings):
    """
    Read the Flower Care sensor and create a complete report.
    """

    stage = stage.strip().lower()
    ideals = get_green_bean_ideals(stage)

    green_bean = Plant(
        name="Green Bean",
        stage=stage,
        ideal_temperature=ideals["temperature"],
        ideal_light=ideals["light"],
        ideal_moisture=ideals["moisture"],
        ideal_fertility=ideals["fertility"],
    )

    health_report = green_bean.check_health(readings)
    advice = generate_advice(health_report)
    status, score = calculate_status(health_report)
    mood = get_plant_mood(score)

    return {
        "plant_name": green_bean.name,
        "stage": stage,
        "ideals": ideals,
        "readings": readings,
        "health_report": health_report,
        "advice": advice,
        "status": status,
        "score": score,
        "mood": mood,
    }


async def terminal_test():
    """
    Test the program without opening Streamlit.
    """

    stage = input(
        "Enter the green bean growth stage: "
    ).strip().lower()

    try:
        report = await get_green_bean_report(stage)

    except Exception as error:
        print(f"Error: {error}")
        return

    print()
    print(
        f"{report['plant_name']} "
        f"({report['stage'].title()})"
    )
    print("-" * 30)

    print(f"Status: {report['status']}")
    print(f"Score: {report['score']}/100")
    print(f"Mood: {report['mood']}")

    print("\nReadings:")

    for name, value in report["readings"].items():
        print(f"{name.title()}: {value}")

    print("\nHealth:")

    for name, value in report["health_report"].items():
        print(f"{name.title()}: {value}")

    print("\nAdvice:")

    if report["advice"]:
        for item in report["advice"]:
            print(f"- {item}")
    else:
        print("- All checked conditions are healthy.")


if __name__ == "__main__":
    asyncio.run(terminal_test())
