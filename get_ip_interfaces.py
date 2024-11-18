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

    interfaces = utils.get_ip_interfaces(connection)
    if interfaces:
        print("_" * 80)
        lines = interfaces.splitlines()
        for line in lines:
            #if "Interface" not in line and "unassigned" not in line and "VirtualPortGroup" not in line:
            if all(keyword not in line for keyword in ["Interface", "unassigned", "VirtualPortGroup"]):
                int_name = line[:22].strip()
                ip = line[23:36].strip()
                print(f"{int_name} - {ip}")
        print("_" * 80)

    if connection:
        connection.disconnect()
