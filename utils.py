import os
def validatePaths(working_directory,pathName,type):
    full_path = os.path.join(working_directory,pathName)
    action = "list"
    if type == "file":
        action = "read"
    out_of_bound_error = f'Error: Cannot {action} "{type}" as it is outside the permitted working directory'
    
    working_directory_abs = os.path.abspath(working_directory)
    full_path_abs = os.path.abspath(full_path)
    common_path = os.path.commonpath([working_directory_abs,full_path_abs])
    
    # print(f"Absolute path of working directory: {working_directory_abs}")
    # print(f"Combined absolute path: {full_path_abs}")
    # print(f"Common path: {common_path}")
    
    if common_path != working_directory_abs:
        return False,out_of_bound_error
    
    return True,full_path_abs


def validateDir(path,directory):
    validCheck = os.path.isdir(path)
    if validCheck:
        return True,""
    return False, f'Error: "{directory}" is not a directory'


def validateFile(path,directory):
    validCheck = os.path.isfile(path)
    if validCheck:
        return True,""
    return False, f'Error: File not found or is not a regular file: "{path}"'
    
    
#Handle any verbose information
def verbose_info(args,user_prompt,usage_metadata):
    if len(args) >= 2:
        if args[1] and args[1] == "--verbose":
            prompt_token_count = usage_metadata.prompt_token_count
            candidate_token_count = usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {candidate_token_count}")