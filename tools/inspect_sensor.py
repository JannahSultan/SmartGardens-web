"""
inspect_sensor.py

Displays the Bluetooth services and characteristics
exposed by the Flower Care sensor.
"""

import asyncio

from bleak import BleakClient


SENSOR_ADDRESS = "5C:85:7E:B0:98:C6"


async def main():
    async with BleakClient(
        SENSOR_ADDRESS
    ) as client:

        print(
            f"Connected: {client.is_connected}"
        )

        for service in client.services:
            print(
                f"\nService: {service.uuid}"
            )

            for characteristic in service.characteristics:
                print(
                    f"  Characteristic: "
                    f"{characteristic.uuid}"
                )

                print(
                    f"  Properties: "
                    f"{characteristic.properties}"
                )


if __name__ == "__main__":
    asyncio.run(
        main()
    )