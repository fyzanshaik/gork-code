from config import MAX_CHAR
import os
from utils import validatePaths

def get_file_content(working_directory, file_path):
    # print("function get_file_content called")
    absolute_full_path = ""
    pathValid,message = validatePaths(working_directory,file_path,"file") 
    if pathValid:
        absolute_full_path = message
    else:
        return message
    
    file_not_found_error = f'Error: File not found or is not a regular file: "{file_path}"'

    checkValidFile = os.path.isfile(absolute_full_path)
    if not checkValidFile:
        return file_not_found_error
    
    file_content = ""
    max_file_content_message = f"[...File '{file_path}' truncated at 10000 characters]"
    
    with open(absolute_full_path,"r") as f:
        file_content = f.read()
        if len(file_content) > MAX_CHAR:
            file_content = file_content[:1001]+" "+max_file_content_message
    
    
    return file_content
    