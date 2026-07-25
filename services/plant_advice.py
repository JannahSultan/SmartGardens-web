"""
plant_advice.py

Generates care advice from a health report.
"""


def generate_advice(health_report):
    """
    Create advice based on low or high measurements.
    """

    advice = []

    temperature = health_report.get(
        "temperature"
    )

    moisture = health_report.get(
        "moisture"
    )

    fertility = health_report.get(
        "fertility"
    )

    light = health_report.get(
        "light"
    )

    if temperature == "Too Low":
        advice.append(
            "Move the plant to a warmer location."
        )

    elif temperature == "Too High":
        advice.append(
            "Move the plant away from excessive heat."
        )

    if moisture == "Too Low":
        advice.append(
            "The soil is too dry. Water the plant slowly."
        )

    elif moisture == "Too High":
        advice.append(
            "The soil is too wet. Allow it to dry before watering again."
        )

    if fertility == "Too Low":
        advice.append(
            "The soil nutrient level is low. Consider adding fertilizer."
        )

    elif fertility == "Too High":
        advice.append(
            "The nutrient level is high. Avoid adding more fertilizer."
        )

    if light == "Too Low":
        advice.append(
            "Move the plant to a brighter location."
        )

    elif light == "Too High":
        advice.append(
            "The plant is receiving too much light. Provide some shade."
        )

    return advice