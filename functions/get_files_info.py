import os

#Input directory and give out the contents of that specific directory with metadata
def get_files_info(working_directory,directory="."):
    full_path = os.path.join(working_directory,directory)
    
    out_of_bound_error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if_not_directory_error = f'Error: "{directory}" is not a directory'
    
    working_directory_abs = os.path.abspath(working_directory)
    full_path_abs = os.path.abspath(full_path)
    common_path = os.path.commonpath([working_directory_abs,full_path_abs])
    
    if common_path != working_directory_abs:
        return out_of_bound_error
    
    validDir = os.path.isdir(full_path_abs)
    
    if not validDir:
        return if_not_directory_error
    
    print(f"Absolute path of working directory: {working_directory_abs}")
    print(f"Combined absolute path: {full_path_abs}")
    print(f"Common path: {common_path}")
    
    dir_list = os.listdir(path=full_path_abs)
    print(dir_list)
    
    current_dir = "current"
    if directory != '.':
        current_dir = directory

    
    file_info_data = f"Result for {current_dir}\n"
    
    for dir in dir_list:
        file_size = os.path.getsize(f"{full_path_abs}/{dir}")
        is_dir = os.path.isdir(f"{full_path_abs}/{dir}")
        file_info_data = file_info_data + f"- {dir}: file_size={file_size}bytes, is_dir={is_dir}\n"
    
    print(file_info_data)
    return file_info_data