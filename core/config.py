from json import load

def load_config():
    with open('config.json') as config_file:
        return load(config_file)