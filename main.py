import asyncio
from playwright.async_api import async_playwright
from geminillm import airesponse
from link import execute
from domindexing import page_state
steps= 30
brave_path= "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
async def run(goal: str, start_url: str):
    async with async_playwright() as pp:
        browser= await pp.chromium.launch(headless=False,slow_mo=500,executable_path=brave_path)
        context= await browser.new_context(viewport={'width': 1280, 'height': 720})
        pag_e= await context.new_page()
        await pag_e.goto(url=start_url,wait_until='domcontentloaded')
        action_history=[]
        for i in range(1,steps+1):
            pagecontext= await page_state(pag_e)
            deci_sion= airesponse(user_goal=goal, page_context=pagecontext, history=action_history)
            result= await execute(decision=deci_sion,page=pag_e)
            action_history.append(f"Step: {i}, Thought: {deci_sion.thought} | Action Taken:"
            f"{deci_sion.action.model_dump()}"
            )


            if result is not None:
                print("Task Finished")
                print(f"Result: {result}")
                break
            else:
                print("Timed out")
        await pag_e.wait_for_event("close")

        
user_goal= input("Describe your task: ")
starting_url= "https://www.google.com"
asyncio.run(run(goal=user_goal,start_url=starting_url))                
