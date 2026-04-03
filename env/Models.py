from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    email_text: str
    history: List[str]

class Action(BaseModel):
    intent: Optional[str] = None
    action: Optional[str] = None
    response: Optional[str] = None

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict = {}
