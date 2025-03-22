import json
import os

class ConfigJSON:
    FILE_PATH = "src/configuration.json"

    @staticmethod
    def load_config():
        """Load config file, or return an empty dict if missing."""
        if not os.path.exists(ConfigJSON.FILE_PATH):
            return {}  # Return empty config if file doesn't exist
        with open(ConfigJSON.FILE_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def get_value(key_path):
        data = ConfigJSON.load_config()
        keys = key_path.split(".")
        temp = data
        for key in keys:
            temp = temp.get(key)
            if temp is None:
                return "Key not found"
        return temp

    @staticmethod
    def update_value(key_path, new_value):
        data = ConfigJSON.load_config()
        keys = key_path.split(".")
        temp = data
        for key in keys[:-1]:  # Traverse up to second last key
            temp = temp.setdefault(key, {})  # Create missing keys if necessary

        temp[keys[-1]] = new_value  # Update the final key

        with open(ConfigJSON.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Updated {key_path} to {new_value}")
