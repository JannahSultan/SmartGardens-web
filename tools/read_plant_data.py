"""
read_plant_data.py

Purpose:
Connect to the Flower Care plant sensor, enable live data mode,
then read temperature, light, moisture, and fertility.

This is the first file that actually gives us useful plant readings.
"""

import asyncio
from bleak import BleakClient


SENSOR_ADDRESS = "5C:85:7E:B0:98:C6"

# This characteristic is used to enable real-time/live data mode.
WRITE_UUID = "00001a00-0000-1000-8000-00805f9b34fb"

# This characteristic contains the actual plant sensor readings.
DATA_UUID = "00001a01-0000-1000-8000-00805f9b34fb"


async def main():
    print("Connecting to Flower Care sensor...")

    async with BleakClient(SENSOR_ADDRESS) as client:
        print("Connected:", client.is_connected)

        # The Flower Care sensor does not always give real data immediately.
        # We first write this command to tell it:
        # "Turn on real-time data mode."
        print("Enabling live data mode...")
        await client.write_gatt_char(WRITE_UUID, bytearray([0xA0, 0x1F]), response=True)

        # Give the sensor a moment to prepare the updated reading.
        await asyncio.sleep(1)

        print("Reading plant data...")
        data = await client.read_gatt_char(DATA_UUID)

        print("Raw data:", data)

        # The sensor sends raw bytes.
        # We decode those bytes into meaningful values.

        # Bytes 0 and 1 store temperature.
        # It is stored as tenths of a degree Celsius.
        temperature = int.from_bytes(data[0:2], byteorder="little", signed=True) / 10

        # Bytes 3 to 6 store light level in lux.
        light = int.from_bytes(data[3:7], byteorder="little")

        # Byte 7 stores soil moisture percentage.
        moisture = data[7]

        # Bytes 8 and 9 store soil fertility / conductivity.
        fertility = int.from_bytes(data[8:10], byteorder="little")

        print()
        print("Decoded plant readings:")
        print(f"Temperature: {temperature} °C")
        print(f"Light: {light} lux")
        print(f"Soil moisture: {moisture}%")
        print(f"Fertility: {fertility} µS/cm")


asyncio.run(main())