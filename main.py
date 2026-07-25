"""
main.py

Combines plant profile information, health analysis,
status, mood, and care advice.
"""

from models.plant import Plant
from models.plant_profiles import get_green_bean_ideals
from models.plant_status import calculate_status
from models.plant_mood import get_plant_mood
from services.plant_advice import generate_advice


def get_green_bean_report(stage, readings):
    """
    Create a complete plant report from supplied sensor readings.
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
