"""
scan_sensor.py

Scans for nearby Bluetooth Low Energy devices.
"""

import asyncio

from bleak import BleakScanner


async def main():
    print(
        "Scanning for Bluetooth devices...\n"
    )

    devices = await BleakScanner.discover(
        timeout=10
    )

    if not devices:
        print(
            "No Bluetooth devices were found."
        )

        return

    for device in devices:
        print(
            f"Name: {device.name}"
        )

        print(
            f"Address: {device.address}"
        )

        print(
            "-" * 40
        )


if __name__ == "__main__":
    asyncio.run(
        main()
    )