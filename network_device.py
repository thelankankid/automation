""" 
Class based python script
"""

import os
from dotenv import load_dotenv
from utils import netutils as net
from utils import inventory as inv


class NetworkDevice:
    """
    Example class for a network device
    """

    def __init__(self, host, ip_address):
        self.hostname = host
        self.ip_address = ip_address
        self.status = "down"

    def bring_up(self):
        """Function bringing up device"""
        self.status = "up"

    def display_status(self):
        """Function displaying device status"""
        print(f"Device {self.hostname} ({self.ip_address}) is {self.status}")

    def ping(self):
        """Function displaying device status"""
        ping = net.ping_device(self.hostname)
        print(ping)

    def check_port(self):
        """Function displaying device status"""
        check_port = net.check_port(self.hostname, 443)
        print(check_port)


if __name__ == "__main__":
    load_dotenv(".env")
    inventory_location = os.getenv("INVENTORY")
    inventory = inv.load_inventory(inventory_location)
    for item in inventory:
        print("-" * 80)
        device = NetworkDevice(item["hostname"], item["ip"])
        device.bring_up()
        device.display_status()
        device.ping()
        device.check_port()
