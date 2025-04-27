import os
import os.path
from os.path import isdir
import pathlib
import Config as CG

Working_conf=""






#CG.load_config()
#CG.config["save_path"] = "E:\\Descargas\\PruebasAnime"
#CG.save_config(CG.config)

#DPath = ("E:\\Descargas\\PruebasAnime")
#DPath2 = ("E:\\Descargas\\Anime")
#Log_Path = "E:\\Descargas")



def userconf():
    Working_conf = CG.load_config()    





def WriteFiles(Data):
    fileRout = os.path.join(CG.config["Log_path"],CG.config["File_Name"])
    if os.path.exists(fileRout):
        with open(fileRout, "a+",encoding="utf-8-sig") as f:
            f.seek(0)            
            f.write(Data)
            f.close
    else:
        with open(fileRout, "a+",encoding="utf-8-sig") as f:                     
            f.write(Data)
            f.close
        



def walking(directory):
    list_Files = os.listdir(directory)
    if list_Files is not None or ("Thumbs.db"):
        for file_name  in list_Files:
            file_path = os.path.join(directory, file_name)
            if file_path != os.path.join(directory,"Thumbs.db"):
                if os.path.isdir(file_path):
                    print("** " + file_name)
                    WriteFiles(file_name + '\n')
                    walking(file_path)
                else:
                    print("-" + file_name)    
                    WriteFiles(file_name + '\n')    



#def Change_Name
# Maps llave ubicacion  valor nombre
userconf()
walking(CG.config["Destiny_Path"])                