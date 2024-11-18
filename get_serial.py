"""
    Main runner script for network automation
"""

import os
from dotenv import load_dotenv
import utils


if __name__ == "__main__":
    load_dotenv(".env")

    IP = os.getenv("IP")
    HOST = os.getenv("HOST")
    DEVICE_TYPE = os.getenv("DEVICE_TYPE")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    connection = utils.device_connect(HOST, DEVICE_TYPE, USERNAME, PASSWORD)

    serial = utils.get_serial_num(connection)
    if serial:
        print("_" * 80)
        print(f"Device serial #: {serial}")
        print("_" * 80)

    if connection:
        connection.disconnect()
