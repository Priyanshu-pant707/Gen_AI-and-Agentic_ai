# creating graph


# state

import os

#1. typed dict

from typing import TypedDict

class State(TypedDict):
    topic:str
    summary:str
    score:str


#2) pydantic approach 

from pydantic import BaseModel,field_validator

class State(BaseModel):
    topic:str
    score:int
    summary:str
    
    @field_validator
    def score_poisitive(cls,v):
        if v<0:
            raise ValueError("Score must be positive")
        
        
        
#3 python data classes

from dataclasses import dataclass,field
@dataclass
class State:
    topic:str=""
    summary :str=""
    message : list=field(default_factory=list)
    
    

#4 langgrpah message state

from langgraph.graph import MessagesState

class State(MessagesState):
    username:str
    language:str