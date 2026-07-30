"""
plant_mood.py

Converts the health score into a plant mood.
"""


def get_plant_mood(score):
    """
    Return a mood based on the plant's health score.
    """

    if score >= 90:
        return "Thriving"

    if score >= 70:
        return "Happy"

    if score >= 50:
        return "Concerned"

    if score >= 25:
        return "Struggling"

    return "Very Unhappy"
