from core.orchestrator import ExecutionOrchestrator

def run_via_http(lang: str, code_file, stdin_file = None) -> dict:
    orchestrator = ExecutionOrchestrator()
    return orchestrator.execute(lang, code_file, stdin_file)

