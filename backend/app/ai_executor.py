# import os
# import asyncio
# from typing import Any
# from .models import RunRequest, RunResult

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# async def call_openai_mock(prompt: str) -> str:
#     """Mocked OpenAI call — replace with real client when available."""
#     await asyncio.sleep(0.2)
#     # Very simple echo mock
#     return f"ECHO: {prompt}" 

# async def handle_run(req: RunRequest) -> RunResult:
#     attempts = 0
#     output = None
#     success = False
#     logs = {}

#     while attempts < (req.max_attempts or 1):
#         attempts += 1
#         logs[f"attempt_{attempts}"] = {"prompt": req.prompt}
#         try:
#             output = await call_openai_mock(req.prompt)
#             success = True
#             logs[f"attempt_{attempts}"]["response"] = output
#             break
#         except Exception as e:
#             logs[f"attempt_{attempts}"]["error"] = str(e)
#             await asyncio.sleep(0.5)

#     return RunResult(success=success, attempts=attempts, output=output, logs=logs)

import subprocess #run code in a subprocess
import asyncio #handle_run need to be async
import os #temp files
import time
from google import genai
from .models import RunRequest, RunResult
import logging,json
key = os.getenv("GOOGLE_API_KEY") 


async def call_ai(prompt:str)->str:
    response = await asyncio.to_thread(genai.chat.completions.create,
        model="gemini-2.5-flash",
        content=prompt,)
    return run_code(response.text)
    


async def handle_run(context:RunRequest)->RunResult:
    attempts = 0
    output = None
    logs = {}
    success = False

    while attempts <= (context.max_attempts or 1):
        attempts+=1
        try:
            output = await call_ai(context.prompt)
            success = True
            break
        except Exception as e:
            logs[f'attempt {attempts} error'] = str(e)
        
    return RunResult(success=success,output=output,logs=logs,attempts=attempts)

async def run_code(code:str)->str:
    filename = f"temp_{time.time()}.py"
    with open(filename,'w') as f:
        f.write(code)
        try:
            result = await asyncio.to_thread(subprocess.run,filename,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=10)
            if result.returncode != 0:
                raise Exception(f"Error in code execution: {result.stderr}")
            return result.stdout
        except subprocess.TimeoutExpired:
            raise Exception("Code execution timed out")
        finally:
            os.remove(filename)
        





        






