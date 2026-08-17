"""
plant_profiles.py

Stores the ideal conditions for each plant stage.
"""

PLANT_PROFILES = {
    "green_bean": {
        "sprout": {
        "temperature": (21, 27),
        "light": (1500, 20000),
        "moisture": (60, 80),
        "fertility": (200, 600),
    },
    "seedling": {
        "temperature": (20, 27),
        "light": (8000, 25000),
        "moisture": (55, 75),
        "fertility": (300, 700),
    },
    "vegetating": {
        "temperature": (20, 30),
        "light": (10000, 30000),
        "moisture": (50, 70),
        "fertility": (400, 800),
    },
    "budding": {
        "temperature": (20, 28),
        "light": (15000, 35000),
        "moisture": (50, 65),
        "fertility": (500, 900),
    },
    "flowering": {
        "temperature": (18, 27),
        "light": (20000, 40000),
        "moisture": (45, 65),
        "fertility": (600, 1000),
    },
    "ripening": {
        "temperature": (18, 26),
        "light": (18000, 35000),
        "moisture": (40, 60),
        "fertility": (500, 800),
    }
        }
}

def get_green_bean_ideals(stage):
    """
    Return the ideal values for a selected growth stage.
    """

    stage = stage.strip().lower()

    if stage not in PLANT_PROFILES:
        valid_stages = ", ".join(
            PLANT_PROFILES.keys()
        )

        raise ValueError(
            f"Invalid stage: {stage}. "
            f"Choose from: {valid_stages}"
        )

    return PLANT_PROFILES[stage]
