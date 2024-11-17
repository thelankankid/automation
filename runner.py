"""
    Main runner script for network automation
"""

import os
from dotenv import load_dotenv
import utils


if __name__ == "__main__":
    load_dotenv(".env")

    IP = os.getenv("IP")
    DEVICE_TYPE = os.getenv("DEVICE_TYPE")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    connection = utils.device_connect(IP, DEVICE_TYPE, USERNAME, PASSWORD)

    cmd_to_run = input("Enter command to run: ")
    cmd = utils.run_command(connection, cmd_to_run)
    if cmd:
        print("_" * 80)
        print(cmd)
        print("_" * 80)

    if connection:
        connection.disconnect()
