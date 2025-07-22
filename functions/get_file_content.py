from config import MAX_CHAR
import os

def get_file_content(working_directory, file_path):
    out_of_bound_error = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    file_not_found_error = f'Error: File not found or is not a regular file: "{file_path}"'
    
    full_path = os.path.join(working_directory,file_path)
    full_path_abs = os.path.abspath(full_path)
    
    working_directory_abs = os.path.abspath(working_directory)
    
    common_path_abs = os.path.commonpath([full_path_abs,working_directory_abs])
    
    if common_path_abs!=working_directory_abs:
        return out_of_bound_error
    
    checkValidFile = os.path.isfile(full_path_abs)
    if not checkValidFile:
        return file_not_found_error
    
    file_content = ""
    max_file_content_message = f"[...File '{file_path}' truncated at 10000 characters]"
    
    with open(full_path_abs,"r") as f:
        file_content = f.read()
        if len(file_content) > MAX_CHAR:
            file_content = file_content[:1001]+" "+max_file_content_message
    
    
    return file_content
    