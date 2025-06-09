from fastapi.applications import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware


from config import SECRET_KEY, DEBUG, SHOULD_USE_SWAGGER, SWAGGER_URL

from controller.executor import executor_controller
from controller.judge import judge_controller

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

app.include_router(executor_controller, prefix="/executor")
app.include_router(judge_controller, prefix="/judge")


