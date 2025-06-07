from core.orchestrator import ExecutionOrchestrator

def run_code_and_capture(lang: str, code_file, stdin_file = None) -> dict:
    orchestrator = ExecutionOrchestrator()
    return orchestrator.execute(lang, code_file, stdin_file)
