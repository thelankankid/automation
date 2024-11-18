"""
    Script to gather Serial number
"""

import os
from dotenv import load_dotenv
from utils import netutils as net


if __name__ == "__main__":
    load_dotenv(".env")

    IP = os.getenv("IP")
    HOST = os.getenv("HOST")
    DEVICE_TYPE = os.getenv("DEVICE_TYPE")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    connection = net.device_connect(HOST, DEVICE_TYPE, USERNAME, PASSWORD)

    serial = net.get_serial_num(connection)
    if serial:
        print("_" * 80)
        print(f"Device serial #: {serial}")
        print("_" * 80)

    if connection:
        connection.disconnect()
