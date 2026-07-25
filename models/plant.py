class Plant:
    """
    Represents a plant and its ideal growing conditions.
    """

    def __init__(
        self,
        name,
        stage,
        ideal_temperature,
        ideal_light,
        ideal_moisture,
        ideal_fertility,
    ):
        self.name = name
        self.stage = stage
        self.ideal_temperature = ideal_temperature
        self.ideal_light = ideal_light
        self.ideal_moisture = ideal_moisture
        self.ideal_fertility = ideal_fertility

    @staticmethod
    def check_value(value, ideal_range):
        minimum, maximum = ideal_range

        if value < minimum:
            return "Too Low"

        if value > maximum:
            return "Too High"

        return "Good"

    def check_health(self, readings):
        health_report = {
            "temperature": self.check_value(
                readings["temperature"],
                self.ideal_temperature,
            ),
            "moisture": self.check_value(
                readings["moisture"],
                self.ideal_moisture,
            ),
            "fertility": self.check_value(
                readings["fertility"],
                self.ideal_fertility,
            ),
        }

        if self.stage != "sprout":
            health_report["light"] = self.check_value(
                readings["light"],
                self.ideal_light,
            )

        return health_report