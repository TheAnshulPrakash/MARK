
class config:

    def get_value(key):
        with open("src/config.txt") as file:
            for line in file:
                if line.startswith(key + "="):
                        return line.strip().split("=")[1]
        return "Key not found"

# Update a value
    def update_value(key, value):
        with open("src/config.txt") as file:
            lines = [f"{key}={value}\n" if line.startswith(key + "=") else line for line in file]
        with open("src/config.txt", "w") as file:
            file.writelines(lines)

# Example usage
#print(get_value("port"))  # Output: COM7
#update_value("theme", "pink")  # Updates theme to "light"
