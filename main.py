import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

print(api_key)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)
text = response.text
usage_metadata = response.usage_metadata

prompt_token_count = usage_metadata.prompt_token_count
candidate_token_count = usage_metadata.candidates_token_count

print(f"Prompt tokens: {prompt_token_count}")
print(f"Response tokens: {candidate_token_count}")