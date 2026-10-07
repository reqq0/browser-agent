from google import genai
from dotenv import load_dotenv
from google.genai import types
from pydantic import BaseModel
load_dotenv()
class agentresponse(BaseModel):
    goal: str
    context: str
def airesponse():
    client= genai.Client()
    prompt=input("Enter prompt")
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
        config= types.GenerateContentConfig(
            system_instruction=("You are an autonomous AI browser agent. Analyze the interactive"
              " DOM elements provided and return the next action required to"
              "achieve the goal."),
                response_mime_type="application/json",
                 response_schema=agentresponse,

    ),
)
    print(response.text)
    return agentresponse.model_validate_json(response.text)
airesponse()