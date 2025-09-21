from fastapi import FastAPI
from . import ai_executor
from google import genai

app = FastAPI(title="Recursive AI Executor (dev)")

@app.on_event("startup")
async def startup_event():
    genai.configure(api_key=ai_executor.key)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/run")
async def run_task(context: ai_executor.RunRequest):
    """Accepts a RunRequest and returns the execution result."""
    result = await ai_executor.handle_run(context)
    return result
