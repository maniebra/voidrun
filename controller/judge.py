from fastapi import APIRouter

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



judge_controller = APIRouter();

@judge_controller.post("/judge-scripted")
async def judge_scripted(
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

@judge_controller.post("/judge/expected")
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
