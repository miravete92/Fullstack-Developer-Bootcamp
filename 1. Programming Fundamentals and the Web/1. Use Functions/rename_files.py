import os

def rename_files():
    file_list = os.listdir(r"./images")
    print(file_list)
    #os.getcwd()
    #os.chdir()
    for file_name in file_list:
        new_file_name = file_name.translate(None,"0123456789")
        print("Old name: "+file_name+" - New Name: "+new_file_name)
        os.rename("./images/"+file_name, "./images/"+new_file_name)
rename_files()    
