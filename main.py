# main.py
import os
import tempfile
from typing import List

from fastapi import FastAPI, Form, UploadFile, HTTPException, WebSocket
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware

from services.http_service import run_via_http
from services.judge_expected_service import judge_expected
from services.judge_scripted_service import judge_with_script
from services.websocket_service import enqueue_websocket_execution

from config import SECRET_KEY, DEBUG, SHOULD_USE_SWAGGER, SWAGGER_URL

app = FastAPI(
    title="VoidRun",
    version="1.0.0",
    docs_url=None if not SHOULD_USE_SWAGGER else SWAGGER_URL,
    redoc_url=None,
    debug=DEBUG
)

if DEBUG:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if SHOULD_USE_SWAGGER:
    @app.get(SWAGGER_URL, include_in_schema=False)
    async def custom_swagger_ui():
        return get_swagger_ui_html(openapi_url=app.openapi_url, title="VoidRun API Docs")

@app.post("/run")
async def run_code(
    lang: str = Form(...),
    code: List[UploadFile] = Form(...),
    stdin: UploadFile = Form(None),
    setup_commands: str = Form(""),
    network: bool = Form(False),
):
    try:
        commands = [c for c in setup_commands.splitlines() if c]
        result = run_via_http(
            lang,
            code,
            stdin,
            setup_commands=commands,
            network_enabled=network,
        )
        return JSONResponse(content=result)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        if DEBUG:
            raise HTTPException(status_code=500, detail=str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/judge/expected")
async def judge_expected_output(
    lang: str = Form(...),
    code: List[UploadFile] = Form(...),
    stdin: UploadFile = Form(None),
    expected_output: str = Form(...),
    setup_commands: str = Form(""),
    network: bool = Form(False),
):
    try:
        commands = [c for c in setup_commands.splitlines() if c]
        result = judge_expected(
            lang,
            code,
            stdin,
            expected_output,
            setup_commands=commands,
            network_enabled=network,
        )
        return JSONResponse(content=result)
    except Exception as e:
        if DEBUG:
            raise HTTPException(status_code=500, detail=str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/judge/scripted")
async def judge_with_custom_script(
    lang: str = Form(...),
    code: List[UploadFile] = Form(...),
    stdin: UploadFile = Form(None),
    judge_script: UploadFile = Form(...),
    setup_commands: str = Form(""),
    network: bool = Form(False),
):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as tmp:
            tmp.write(judge_script.file.read())
            tmp.flush()
            commands = [c for c in setup_commands.splitlines() if c]
            result = judge_with_script(
                lang,
                code,
                stdin,
                tmp.name,
                setup_commands=commands,
                network_enabled=network,
            )
        return JSONResponse(content=result)
    except Exception as e:
        if DEBUG:
            raise HTTPException(status_code=500, detail=str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.websocket("/ws/run")
async def websocket_run(websocket: WebSocket):
    await websocket.accept()
    await enqueue_websocket_execution(websocket, "python", None, None, None, False)
    await websocket.close()
