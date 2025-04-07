import os 
import re


Path1 = (r"E:\Descargas\Anime 2\Donwload_test")



def get_name(Path):
    list_file = os.listdir(Path)
    for file_name in list_file:
        Change_name(file_name)



def Change_name(Name):
    #pattern = (r"(\d{1,4})_(\d+) _?[a-zA-Z0-9]*\.(\w+)")
    pattern = (r"(\d+)[ _](\d{1,3})(?:[ _]\w*)?\.(.+)")
    match =re.match(pattern,Name)
    if not match:
        print(f"Skipping:{Name} (Invalid Format)")
    else:
        print(f"Formated:{Name} (New named)")    
        


    num1, num2, ext = match.groups()
    print(00)
get_name(Path1)

