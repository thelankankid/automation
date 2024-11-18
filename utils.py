"""
Utility functions for network device interaction using Netmiko.
"""

import netmiko


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
