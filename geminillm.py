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
3. Always state your reasoning in the "thought" field.
4. Do NOT repeat an action that you already tried and failed, or one that you already completed in the history. If the goal is achieved, you MUST use the 'done' action.
"""
def airesponse(user_goal: str, page_context: str, history: list=None):
    client= genai.Client()
    history_text="\n".join(history) if history else "No previous action taken yet"
    prompt=f""""
    Goal: {user_goal}
    Context: {page_context}
Action history: {history}

    """
    response=client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt,
        config= types.GenerateContentConfig(
            system_instruction=(rule),
                response_mime_type="application/json",
                 response_schema=Response,
                 temperature=0.7,

    ),
)
    print(response.text)
    return Response.model_validate_json(response.text)
