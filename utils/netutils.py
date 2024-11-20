"""
Utility functions for network device interaction using Netmiko.
"""

import netmiko
import subprocess
import re
import socket

def device_connect(host, device_type, username, password):
    """
    Establishes a connection to a network device.

    Args:
        ip (str): The IP address of the device.
        device_type (str): The type of device (e.g., 'cisco_ios').
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        netmiko.ConnectHandler: The Netmiko connection object or None if connection fails.
    """
    try:
        net_connect = netmiko.ConnectHandler(
            # ip=ip,
            host=host,
            device_type=device_type,
            username=username,
            password=password,
            port=22,
        )
        # print(f"Successfully connected to {ip}")
        print(f"Successfully connected to {host}")
        return net_connect
    except netmiko.NetmikoTimeoutException as e:
        print(f"Connection timed out for {host}: {e}")
        return None
    except netmiko.NetmikoAuthenticationException as e:
        print(f"Authentication failed for {host}: {e}")
        return None
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        return None


def get_log(net_connect):
    """
    Retrieves the device log.

    Args:
        net_connect (netmiko.ConnectHandler): The Netmiko connection object.

    Returns:
        str: The log output or None if an error occurs.
    """
    if net_connect:
        try:
            logs = net_connect.send_command("show log")
            return logs
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None


def show_version(net_connect):
    """
    Retrieves the device version information.

    Args:
        net_connect (netmiko.ConnectHandler): The Netmiko connection object.

    Returns:
        str: The version information or None if an error occurs.
    """
    if net_connect:
        try:
            cmd = net_connect.send_command("show version")
            return cmd
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None


def get_serial_num(net_connect):
    """
    Retrieves Serial number from Cisco device.

    Args:
        net_connect (netmiko.ConnectHandler): The Netmiko connection object.

    Returns:
        str: The version information or None if an error occurs.
    """
    if net_connect:
        try:
            sho_ver = net_connect.send_command("show version | in Processor")
            serial_num = sho_ver[19:30]
            return serial_num
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None


def get_ip_interfaces(net_connect):
    """
    Retrieves IP interfaces from Cisco device.

    Args:
        net_connect (netmiko.ConnectHandler): The Netmiko connection object.

    Returns:
        str: The version information or None if an error occurs.
    """
    if net_connect:
        try:
            interfaces = net_connect.send_command("show ip interface brief")
            # serial_num = sho_ver[19:30]
            return interfaces
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None


def run_command(net_connect, command):
    """
    Runs a specified command on the network device.

    Args:
        net_connect (netmiko.ConnectHandler): The Netmiko connection object.
        command (str): The command to be executed.

    Returns:
        str: The command output or None if an error occurs.
    """
    if net_connect:
        try:
            cmd = net_connect.send_command(command)
            return cmd
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None

def get_interface_config(net_connect, interface):
    if net_connect:
        try:
            interface_config = net_connect.send_command("show run interface "+ interface )
            return interface_config
        except Exception as e:
            print(f"Error executing command: {e}")
            return None
    else:
        print("Connection object is invalid.")
        return None

def parse_ping_result(result):

    rtt_pattern = r"round-trip min/avg/max/stddev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms"
    pkt_loss_pattern = r"(\d+\.\d+\%) packet loss"

    pkt_loss_match = re.search(pkt_loss_pattern, result)
    rtt_match = re.search(rtt_pattern, result)

    formatted_result = ""
    if pkt_loss_match:
        pkt_loss = pkt_loss_match.group(1)
        formatted_result += (f"\tPacket loss: {pkt_loss}\n")
    if rtt_match:
        min_rtt = rtt_match.group(1)
        avg_rtt = rtt_match.group(2)
        max_rtt = rtt_match.group(3)
        formatted_result += (f"\tMinimum RTT: {min_rtt} ms\n")
        formatted_result += (f"\tAverage RTT: {avg_rtt} ms\n")
        formatted_result += (f"\tMaximum RTT: {max_rtt} ms\n")
    
    final_output = ("="*20 + " Reachability test " + "="*20 + "\n")
    final_output += formatted_result
    return final_output

def ping_device(host):
    """Pings a host and returns the result."""
    try:
        result = subprocess.run(
            ["ping", "-c", "2", host],
            capture_output=True,
            text=True
        )
        #print(result)
        if result.returncode == 0:
            return parse_ping_result(result.stdout)
            
        else:
            return f"Ping failed:\n{result.stderr}"
    except FileNotFoundError:
        return "Error: The 'ping' command is not found"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def check_port(host, port):
    """Connects to a port and returns the result."""
    try:
        with socket.create_connection((host, port), timeout=2):
            return f"Port {port} is open"
    except (socket.timeout, ConnectionRefusedError):
        return f"Port {port} is NOT open"
