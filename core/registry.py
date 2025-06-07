from executors.python import PythonExecutor
from executors.c import CExecutor
from executors.ts_js import TSJSExecutor

EXECUTOR_REGISTRY = {
    "python": PythonExecutor,
    "c": CExecutor,
    "js": TSJSExecutor,
    "ts": TSJSExecutor
}

def get_executor_class(lang: str):
    if lang not in EXECUTOR_REGISTRY:
        raise ValueError(f"Unsupported language: {lang}")
    return EXECUTOR_REGISTRY[lang]
