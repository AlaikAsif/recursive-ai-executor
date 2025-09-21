from pydantic import BaseModel
from typing import Optional

class RunRequest(BaseModel):
    prompt: str
    max_attempts: Optional[int] = 5

class RunResult(BaseModel):
    success: bool
    attempts: int
    output: Optional[str]
    logs: Optional[dict]
