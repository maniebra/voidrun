from generics.base_sandbox import BaseSandbox
from abc import ABC, abstractmethod

class BaseExecutor(ABC):
    def __init__(self, sandbox: BaseSandbox, code_file: str, stdin_file: str):
        self.sandbox = sandbox
        self.code_file = code_file
        self.stdin_file = stdin_file

    @abstractmethod
    def get_execution_command(self) -> str:
        """
        Returns the command to execute the code (inside sandbox).
        This should not include sandbox wrapper logic.
        """
        pass

    def run(self) -> dict:
        """
        Orchestrates code execution via the provided sandbox.
        """
        command = self.get_execution_command()
        return self.sandbox.run(command, stdin_path=self.stdin_file)

