# config_reader.py

def load_properties(filepath):
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip() == "" or line.startswith("#"):
                continue
            key, value = line.strip().split("=", 1)
            config[key.strip()] = value.strip()
    return config
