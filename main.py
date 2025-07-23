import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from config import SYSTEM_PROMPT_FUNCTION_CALLING
from functions.schema_function import available_functions
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info

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
    
#Handle any verbose information
def verbose_info(args,user_prompt,usage_metadata):
    if len(args) >= 2:
        if args[1] and args[1] == "--verbose":
            prompt_token_count = usage_metadata.prompt_token_count
            candidate_token_count = usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {candidate_token_count}")

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    print(api_key)

    args = sys.argv[1:]
    print(args)
    if not args:
        print("Gork CLI")
        print('\nUsage: python main.py "Add prompt here!"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    client = genai.Client(api_key=api_key)

    user_prompt = "".join(args[0])

    messages = [
        types.Content(role="User", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools=[available_functions],system_instruction=SYSTEM_PROMPT_FUNCTION_CALLING)
    )
    
    usage_metadata = response.usage_metadata
    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call)
            if function_call_result.parts[0].function_response.response:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise Exception("Some error")
    else:
        print(f"Gemini response: {response.text}")

    
    verbose_info(args,user_prompt,usage_metadata)

    
if __name__ == "__main__":
    main()