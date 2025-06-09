from fastapi import APIRouter, Form, UploadFile, HTTPException, WebSocket
from fastapi.responses import JSONResponse

from config import DEBUG
from services.websocket_service import enqueue_websocket_execution
from services.http_service import run_via_http

executor_controller = APIRouter();

@executor_controller.post("/run")
async def run_code(
    self,
    lang: str = Form(...),
    code: list[UploadFile] = Form(...),
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

@executor_controller.websocket("/ws/run")
async def websocket_run(websocket: WebSocket):
    await websocket.accept()
    await enqueue_websocket_execution(websocket, "python", None, None, None, False)
    await websocket.close()
