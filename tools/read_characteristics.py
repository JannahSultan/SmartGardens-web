"""
read_characteristics.py

Purpose:
Read every characteristic that supports reading and display
its raw data.

This helps us determine which characteristic stores the
plant sensor measurements.
"""

import asyncio
from bleak import BleakClient

SENSOR_ADDRESS = "5C:85:7E:B0:98:C6"


async def main():

    async with BleakClient(SENSOR_ADDRESS) as client:

        print("Connected!\n")

        for service in client.services:

            print(f"Service: {service.uuid}")

            for characteristic in service.characteristics:

                # Only attempt to read characteristics that support reading.
                if "read" in characteristic.properties:

                    try:
                        value = await client.read_gatt_char(characteristic.uuid)

                        print(f"Characteristic: {characteristic.uuid}")
                        print(f"Raw bytes: {value}")
                        print()

                    except Exception as e:

                        print(f"Characteristic: {characteristic.uuid}")
                        print(f"Could not read ({e})")
                        print()


asyncio.run(main())