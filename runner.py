"""
    Main runner script for network automation
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

    prompt = ""
    while prompt != "x":
        cmd_to_run = input("Enter command to run: ")
        cmd = net.run_command(connection, cmd_to_run)
        if cmd:
            print("_" * 80)
            print(cmd)
            print("_" * 80)
        prompt = input("Press Enter to Continue or x to exit: ")

    if connection:
        connection.disconnect()
