from pydantic import BaseModel
from typing import Literal,Union

class Click(BaseModel):
    actiontype: Literal['click']='click'
    element_id: int
class Type(BaseModel):
    actiontype: Literal['type']='type' 
    text: str
    element_id: int
class Navigate(BaseModel):
    actiontype: Literal['navigate']='navigate'
    url: str
class Scroll(BaseModel):
    actiontype: Literal['scroll']='scroll'
    direction: Literal['up','down']
    amount: int=500
class Done(BaseModel):
    actiontype: Literal['done']='done'
    answer: str
class Hover(BaseModel):
    actiontype: Literal['hover']='hover'
    element_id: int 
class Response(BaseModel):
    action: Union[Type,Navigate,Scroll,Done,Hover,Click]
    thought: str

