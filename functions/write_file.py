import os

def write_file(working_directory, file_path, content):
    out_of_bound_error = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    success_message = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    full_path = os.path.join(working_directory,file_path)
    full_path_abs = os.path.abspath(full_path)
    
    working_directory_abs = os.path.abspath(working_directory)
    
    common_path = os.path.commonpath([full_path_abs,working_directory_abs])
    
    if common_path != working_directory_abs:
        return out_of_bound_error
    
    # print(f"Full path: {full_path_abs}")
    dirName = os.path.dirname(file_path)
    # print(dirName)
    directoryPath = os.path.join(working_directory_abs,dirName)
    checkDirExist = os.path.exists(directoryPath)
    # print(checkDirExist)
    
    # checkFileExist = os.path.exists(full_path_abs)
    
    if not checkDirExist:
        print("Creating directory")
        os.makedirs(directoryPath)
    
    with open(full_path_abs,"w") as f:
        f.write(content)
        
    return success_message