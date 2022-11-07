import os
import shutil
from_dir = "C:/Users/rahil/Downloads"
to_dir = "C:/Users/rahil/OneDrive/Documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)
    #print(name)
    #print(extention)
    if extention == "":
        continue
    if extention in ['.csv']:
        path1 = from_dir + '/' + file_name #Downloads/ImageName1.jpg
        path2 = to_dir + '/' + "CSV_Files" #D:/My Files/Image_File
        path3 = to_dir + '/' + "CSV_Files" + '/' + file_name #D:/MyFiles/Image_Files/Im ageName1.jpg
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving" + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print(path1)
            print(path3)