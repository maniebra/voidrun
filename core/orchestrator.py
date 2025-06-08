import os
from utils.fs import (
    create_sandbox_dir,
    save_file,
    save_files,
    ensure_empty_stdin,
    cleanup_dir,
)
from core.registry import get_executor_class
from sandbox.firejail import FirejailSandbox

class ExecutionOrchestrator:
    def __init__(self, timeout: int = 5, max_processes: int = 10):
        self.timeout = timeout
        self.max_processes = max_processes

    def execute(
        self,
        lang: str,
        code_files,
        stdin_file=None,
        setup_commands=None,
        network_enabled: bool = False,
    ) -> dict:
        sandbox_root = create_sandbox_dir()
        try:
            if not isinstance(code_files, list):
                code_files = [code_files]

            filenames = save_files(sandbox_root, code_files)
            stdin_path = os.path.join(sandbox_root, "stdin.txt")

            if stdin_file:
                save_file(stdin_path, stdin_file)
            else:
                ensure_empty_stdin(stdin_path)

            ExecutorClass = get_executor_class(lang)
            sandbox = FirejailSandbox(
                working_dir=sandbox_root,
                timeout=self.timeout,
                max_processes=self.max_processes,
                network_enabled=network_enabled,
            )
            executor = ExecutorClass(
                sandbox=sandbox,
                code_files=filenames,
                stdin_file="stdin.txt",
                setup_commands=setup_commands,
            )
            return executor.run()

        finally:
            cleanup_dir(sandbox_root)
