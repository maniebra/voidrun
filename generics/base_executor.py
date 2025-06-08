from generics.base_sandbox import BaseSandbox
from abc import ABC, abstractmethod

class BaseExecutor(ABC):
    def __init__(
        self,
        sandbox: BaseSandbox,
        code_files: list[str],
        stdin_file: str,
        setup_commands: list[str] | None = None,
    ):
        self.sandbox = sandbox
        self.code_files = code_files
        self.stdin_file = stdin_file
        # commands to be executed before running the main program
        self.setup_commands = setup_commands or []

    @abstractmethod
    def get_execution_command(self) -> str:
        """
        Returns the command to execute the code (inside sandbox).
        This should not include sandbox wrapper logic.
        """
        pass

    def run(self) -> dict:
        """Orchestrates optional setup and code execution via the sandbox."""
        setup_results = []
        for cmd in self.setup_commands:
            result = self.sandbox.run(cmd, stdin_path=self.stdin_file)
            setup_results.append({"command": cmd, **result})
            if result.get("exit_code") != 0:
                return {"setup_results": setup_results}

        command = self.get_execution_command()
        execution_result = self.sandbox.run(command, stdin_path=self.stdin_file)
        return {"setup_results": setup_results, **execution_result}

