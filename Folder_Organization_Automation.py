from os import listdir
from os.path import isfile, join
import os
import shutil
def sort_files_in_a_folder(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    for file in files:
        filetype=file.split('.')[1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name = f'{mypath}/{filetype}_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    for file in files:
        src_path = f'{mypath}/{file}'
        filetype=file.split('.')[1]
        if filetype in filetype_folder_dict:
            dest_path=filetype_folder_dict[str(filetype)]
            shutil.move(src_path,dest_path)
            print(f'{src_path}>>>{dest_path}')

if __name__=="__main__":
    direct = input("Please enter the directory:")
    mypath=direct
    sort_files_in_a_folder(mypath)
    input('Press ENTER to exit')
