import os
import asyncio
from typing import Any
from .models import RunRequest, RunResult

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def call_openai_mock(prompt: str) -> str:
    """Mocked OpenAI call — replace with real client when available."""
    await asyncio.sleep(0.2)
    # Very simple echo mock
    return f"ECHO: {prompt}" 

async def handle_run(req: RunRequest) -> RunResult:
    attempts = 0
    output = None
    success = False
    logs = {}

    while attempts < (req.max_attempts or 1):
        attempts += 1
        logs[f"attempt_{attempts}"] = {"prompt": req.prompt}
        try:
            output = await call_openai_mock(req.prompt)
            success = True
            logs[f"attempt_{attempts}"]["response"] = output
            break
        except Exception as e:
            logs[f"attempt_{attempts}"]["error"] = str(e)
            await asyncio.sleep(0.5)

    return RunResult(success=success, attempts=attempts, output=output, logs=logs)
