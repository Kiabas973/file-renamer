import os
import shutil

folder_path = os.getcwd()
print(folder_path)
Nom=input("Name > ")
Saison="S"+input("Saison > ")
Vo=input("Vo > ")
Resolution=input("Resolution > ")+"p"
i=1

def rename(ext):
    if i < 10:
        fileNewname_path = (path+"\\"+Nom+"."+Saison+"E0"+str(i)+"."+Vo+"."+Resolution+ext)
    else:
        fileNewname_path = (path+"\\"+Nom+"."+Saison+"E"+str(i)+"."+Vo+"."+Resolution+ext)
    shutil.move(filename_path, fileNewname_path)
    print(filename+" > "+fileNewname_path)

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        filename_path = (path+"\\"+filename)
        if ".mp4" in filename_path:
            rename(".mp4")
            i+=1
        elif ".mkv" in filename_path:
            rename(".mkv")
            i+=1