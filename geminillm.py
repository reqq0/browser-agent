from google import genai
from dotenv import load_dotenv
from google.genai import types
from pydantic import BaseModel
from agentaction import Response
load_dotenv()
rule="""
You are an autonomous AI browser agent. Your job is to achieve the user's goal by analyzing the provided interactive DOM elements on the page and choosing the correct next action.

Rules:
1. Select target elements using their exact integer element_id ([1], [2], etc.).
2. Choose 'done' when the user goal is completely achieved or summarized.
"""
def airesponse():
    client= genai.Client()
    prompt=input("Enter prompt")
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
        config= types.GenerateContentConfig(
            system_instruction=(rule),
                response_mime_type="application/json",
                 response_schema=Response,

    ),
)
    print(response.text)
    return Response.model_validate_json(response.text)
