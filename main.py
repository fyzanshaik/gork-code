import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from config import SYSTEM_PROMPT_FUNCTION_CALLING,MAX_LOOP_CALL
from functions.schema_function import available_functions
from functions.call_function import call_function
from utils import verbose_info
    
def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    # print(api_key)

    args = sys.argv[1:]
    # print(args)
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
    
    for i in range(1,MAX_LOOP_CALL+1):
        # print(f"Iterating {i}th time")
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools=[available_functions],system_instruction=SYSTEM_PROMPT_FUNCTION_CALLING)
        )
        usage_metadata = response.usage_metadata
        for candidate in response.candidates:
            messages.append(candidate.content)
        
        function_responses_list = []
        # verbose_info(args,user_prompt,usage_metadata)
        
        if response.function_calls:
            for function_call in response.function_calls:
                # print(f"Calling function: {function_call.name} with arguments: ({function_call.args})\n")
                function_call_result = call_function(function_call,args)
                function_responses_list.append(
                     types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": function_call_result}
                    )
                )
            tool_message = types.Content(
                role="tool",
                parts=function_responses_list
            )
            messages.append(tool_message)
        elif response.text:
            print(f"Coding agent response: {response.text}")
            break
        else:
            print("Retrying")
            continue
    
   

    
if __name__ == "__main__":
    main()