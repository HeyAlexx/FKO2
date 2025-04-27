import json
import os



CONFIG_FILE = r"G:\Coding Files\Python\FKO2\config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return default_config

def save_config(config):
    with open(CONFIG_FILE, "w")  as file: 
        json.dump(config,file,indent=4)




default_config = {
        "Downloads_Path": r"E:\Download\path",
        "Log_path":  r"E:\Descargas", 
        "Destiny_Path" : r"E:\Descargas\Anime",
        "max_files": 10,
        "enable_logging": True,
        "File_Name": "Test1.txt"
}

# Usage
save_config(default_config)
config = load_config()
print(default_config)

# Update and save new config

#"save_path": "default_path/"


