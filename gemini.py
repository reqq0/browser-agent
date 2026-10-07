from google import genai
from dotenv import load_dotenv
from gemini import types

load_dotenv()
client= genai.Client()
prompt=input("Enter prompt")
response=client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt
)
print("Ai response")
print(response.text)