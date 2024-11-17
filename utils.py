import netmiko

def device_connect(ip, device_type, username, password):
    try:
        net_connect = netmiko.ConnectHandler(
            ip=ip,
            device_type=device_type,
            username=username,
            password=password,
            port=22
        )
        print(f"Successfully connected to {ip}")
        return net_connect
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
        return None

def get_log(net_connect):
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
