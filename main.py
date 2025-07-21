import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

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
        model='gemini-2.0-flash-001', contents=messages
    )
    
    text = response.text
    usage_metadata = response.usage_metadata
    print(f"Gemini response: {text.strip()}")

    if len(args) >= 2:
        if args[1] and args[1] == "--verbose":
            prompt_token_count = usage_metadata.prompt_token_count
            candidate_token_count = usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {candidate_token_count}")
    

    
if __name__ == "__main__":
    main()