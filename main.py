from fastapi import FastAPI, Form, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from core.orchestrator import ExecutionOrchestrator

app = FastAPI(title="VoidRun", version="1.0.0")

orchestrator = ExecutionOrchestrator(timeout=5, max_processes=10)

@app.post("/run")
async def run_code(
    lang: str = Form(...),
    code: UploadFile = Form(...),
    stdin: UploadFile = Form(None)
):
    try:
        result = orchestrator.execute(lang, code, stdin)
        return JSONResponse(content=result)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
