import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    out_of_bound_error = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    file_not_exist_error = f'Error: File "{file_path}" not found.'
    if_not_py_error = f'Error: "{file_path}" is not a Python file.'
    full_path = os.path.join(working_directory,file_path)
    full_path_abs = os.path.abspath(full_path)
    
    working_directory_abs = os.path.abspath(working_directory)
    
    common_path = os.path.commonpath([full_path_abs,working_directory_abs])
    
    if common_path != working_directory_abs:
        return out_of_bound_error
    
    checkFilePath = os.path.exists(full_path_abs)
    if not checkFilePath:
        return file_not_exist_error
    
    fileName = os.path.basename(file_path)
    print(fileName[len(fileName)-2:])
    if fileName[len(fileName)-2:] != "py":
        return if_not_py_error
    
    args_to_pass = ["python3",fileName] + args
    print(args_to_pass)
    result_message = ""
    try:
        result_process = subprocess.run(args=args_to_pass,capture_output=True,timeout=30,cwd=working_directory_abs)
        if result_process.returncode != 0:
            result_message.join(f"Process exited with code {result_process.returncode}")
        stdout = result_process.stdout
        stderr = result_process.stderr
        stderr_message = f"{result_message}\nSTDERR: {stderr}"

        if len(stderr) > 0:
            return stderr_message
        if len(stdout) == 0:
            return "No output produced."
        else:
            stdout_message = f"{result_message}\nSTDOUT: {stdout}"
            return stdout_message
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
        