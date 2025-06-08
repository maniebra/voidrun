from core.orchestrator import ExecutionOrchestrator


def run_via_http(
    lang: str,
    code_files,
    stdin_file=None,
    setup_commands=None,
    network_enabled: bool = False,
) -> dict:
    orchestrator = ExecutionOrchestrator()
    return orchestrator.execute(
        lang,
        code_files,
        stdin_file=stdin_file,
        setup_commands=setup_commands,
        network_enabled=network_enabled,
    )

