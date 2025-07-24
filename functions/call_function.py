from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info
from google.genai import types

def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    args_dict = function_call_part.args
    args_dict["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {func_name}({args_dict})")
    else:
        print(f" - Calling function: {func_name}")

    match func_name:
        case "run_python_file":
            result = run_python_file(**args_dict)
            return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
            name=func_name,
            response={"result": result},
            )
        ],
    )
        case "get_file_content":
            result = get_file_content(**args_dict)
            return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
            name=func_name,
            response={"result": result},
            )
        ],
    )
        case "write_file":
            result = write_file(**args_dict)
            return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
            name=func_name,
            response={"result": result},
            )
        ],
    )
        case "get_files_info":
            result = get_files_info(**args_dict)
            return types.Content(
            role="tool",
            parts=[
            types.Part.from_function_response(
            name=func_name,
            response={"result": result},
            )
        ],
    )
        case _:
            return types.Content(
                role="tool",
                parts=[
                types.Part.from_function_response(
                name=func_name,
                response={"error": f"Unknown function: {func_name}"},
            )
            ],
        )