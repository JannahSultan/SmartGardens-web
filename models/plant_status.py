"""
plant_status.py

Calculates the plant's health score and overall status.
"""


def calculate_status(health_report):
    """
    Calculate a score out of 100.

    Every unhealthy measurement removes 25 points.
    """

    total_measurements = len(
        health_report
    )

    if total_measurements == 0:
        return "Unknown", 0

    good_measurements = sum(
        1
        for result in health_report.values()
        if result == "Good"
    )

    score = round(
        (
            good_measurements
            / total_measurements
        )
        * 100
    )

    if score == 100:
        status = "Healthy"

    elif score >= 50:
        status = "Needs Attention"

    else:
        status = "Unhealthy"

    return status, score