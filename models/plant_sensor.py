"""
plant_sensor.py

Purpose:
Defines the PlantSensor class.

This class is responsible for:
1. Connecting to the plant sensor
2. Reading the raw sensor data
3. Converting the raw bytes into meaningful measurements

Any other file in the project can create a PlantSensor object
instead of dealing with Bluetooth directly.
"""

import asyncio
from bleak import BleakClient


class PlantSensor:
    """
    Represents one Flower Care plant sensor.
    """

    # Constructor
    #
    # Runs whenever we create a PlantSensor object.
    #
    # Example:
    #
    # sensor = PlantSensor("5C:85:7E:B0:98:C6")
    #
    def __init__(self, address):

        # Save the Bluetooth address.
        self.address = address

        # Characteristic used to enable live readings.
        self.WRITE_UUID = "00001a00-0000-1000-8000-00805f9b34fb"

        # Characteristic that stores the plant measurements.
        self.DATA_UUID = "00001a01-0000-1000-8000-00805f9b34fb"


    async def get_readings(self):
        """
        Connects to the sensor and returns the current readings.

        Returns:
            dictionary containing
                temperature
                light
                moisture
                fertility
        """

        async with BleakClient(self.address) as client:

            # Enable live data mode.
            await client.write_gatt_char(
                self.WRITE_UUID,
                bytearray([0xA0, 0x1F]),
                response=True
            )

            # Give the sensor one second to update.
            await asyncio.sleep(1)

            # Read the raw bytes.
            data = await client.read_gatt_char(self.DATA_UUID)

            # Decode the bytes.

            temperature = int.from_bytes(
                data[0:2],
                byteorder="little",
                signed=True
            ) / 10

            light = int.from_bytes(
                data[3:7],
                byteorder="little"
            )

            moisture = data[7]

            fertility = int.from_bytes(
                data[8:10],
                byteorder="little"
            )

            # Return all readings as a dictionary.
            return {
                "temperature": temperature,
                "light": light,
                "moisture": moisture,
                "fertility": fertility
            }