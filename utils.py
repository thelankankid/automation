"""
Utility functions for network device interaction using Netmiko.
"""

import netmiko


def device_connect(ip, device_type, username, password):
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
            ip=ip,
            device_type=device_type,
            username=username,
            password=password,
            port=22,
        )
        print(f"Successfully connected to {ip}")
        return net_connect
    except netmiko.NetmikoTimeoutException as e:
        print(f"Connection timed out for {ip}: {e}")
        return None
    except netmiko.NetmikoAuthenticationException as e:
        print(f"Authentication failed for {ip}: {e}")
        return None
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
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
