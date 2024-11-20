import yaml


def load_inventory(file_path):
    """
    Load the inventory from a YAML file and return it as a dictionary.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        list: A list of dictionaries representing the inventory.
    """
    with open(file_path, "r", encoding="utf8") as file:
        # Load the YAML file into a Python object
        inventory_raw = yaml.safe_load(file)

        # Optional: Validate or process inventory as needed
        inventory = []
        for device in inventory_raw:
            # Extract device details
            fqdn = device["hostname"]
            hostname = fqdn.split(".")[0]  # Extract the short hostname
            ip = device.get("ip", None)  # Use .get() in case "ip" is missing
            device_type = device["type"]

            # Append the processed device to the result list
            inventory.append(
                {
                    "hostname": fqdn,
                    "short_hostname": hostname,
                    "ip": ip,
                    "type": device_type,
                }
            )

        return inventory
