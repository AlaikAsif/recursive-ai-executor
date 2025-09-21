from fastapi import FastAPI
from . import ai_executor

app = FastAPI(title="Recursive AI Executor (dev)")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/run")
async def run_task(payload: ai_executor.RunRequest):
    """Accepts a RunRequest and returns the execution result."""
    result = await ai_executor.handle_run(payload)
    return result
