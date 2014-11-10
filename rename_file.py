import os

def rename_files():
    file_list=os.listdir(r"F:\Udacity proj\prank")
    print(file_list)
    saved_path=os.getcwd()
    #print("current working in"+saved_path)
    os.chdir(r"F:\Udacity proj\prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)              

rename_files()    
