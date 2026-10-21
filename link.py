import asyncio
from agentaction import Response, Type
from playwright.async_api import Page

async def execute(decision: Response, page: Page):
      act=decision.action
      act_type=act.actiontype
            
      if act_type == 'click':
            selector=f'[target-id="{act.element_id}"]'
            await page.wait_for_selector(selector=selector,state="visible",timeout=5000)
            await page.click(selector)
      elif isinstance(act, Type):
            selector=f'[target-id="{act.element_id}"]'
            await page.wait_for_selector(selector=selector,state='visible',timeout=5000)
            await page.fill(selector, act.text)
      elif act_type == 'navigate':
            await page.goto(act.url,wait_until='domcontentloaded')
      elif act_type == 'done':
            print("Task completed")
            print(f"{act.answer}")
            return act.answer
      elif act_type == 'hover':
            selector=f'[target-id="{act.element_id}"]'
            await page.wait_for_selector(selector=selector,state='visible',timeout=5000)
            await page.hover(selector=selector)
      elif act_type == 'scroll':
            value= act.amount if act.direction=='down' else -act.amount
            await page.evaluate(f"window.scrollBy(0,{value})")
      await asyncio.sleep(2)
      return None






