import os
from utils.fs import (
    create_sandbox_dir,
    save_file,
    ensure_empty_stdin,
    cleanup_dir
)
from core.registry import get_executor_class
from sandbox.firejail import FirejailSandbox

class ExecutionOrchestrator:
    def __init__(self, timeout: int = 5, max_processes: int = 10):
        self.timeout = timeout
        self.max_processes = max_processes

    def execute(self, lang: str, code_file, stdin_file = None) -> dict:
        sandbox_root = create_sandbox_dir()
        try:
            code_filename = code_file.filename
            code_path = os.path.join(sandbox_root, code_filename)
            stdin_path = os.path.join(sandbox_root, "stdin.txt")

            save_file(code_path, code_file)
            if stdin_file:
                save_file(stdin_path, stdin_file)
            else:
                ensure_empty_stdin(stdin_path)

            ExecutorClass = get_executor_class(lang)
            sandbox = FirejailSandbox(
                working_dir=sandbox_root,
                timeout=self.timeout,
                max_processes=self.max_processes
            )
            executor = ExecutorClass(
                sandbox=sandbox,
                code_file=code_filename,
                stdin_file="stdin.txt"
            )
            return executor.run()

        finally:
            cleanup_dir(sandbox_root)
