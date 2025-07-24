import os
from utils import validatePaths,validateDir

#Input directory and give out the contents of that specific directory with metadata
def get_files_info(working_directory,directory="."):
    absolute_full_path = ""
    pathValid,message = validatePaths(working_directory,directory,"directory") 
    if pathValid:
        absolute_full_path = message
    else:
        return message
    
    dirValid,message = validateDir(absolute_full_path,directory)
       
    if not dirValid:
        return message
    
    dir_list = os.listdir(path=absolute_full_path)
    # print(dir_list)
    
    current_dir = "current"
    if directory != '.':
        current_dir = directory

    
    file_info_data = f"Result for {current_dir}\n"
    
    for dir in dir_list:
        file_size = os.path.getsize(f"{absolute_full_path}/{dir}")
        is_dir = os.path.isdir(f"{absolute_full_path}/{dir}")
        file_info_data = file_info_data + f"- {dir}: file_size={file_size}bytes, is_dir={is_dir}\n"
    
    # print(file_info_data)
    return file_info_data