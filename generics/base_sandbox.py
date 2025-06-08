from abc import ABC, abstractmethod

class BaseSandbox(ABC):
    def __init__(self, working_dir: str, network_enabled: bool = False):
        self.working_dir = working_dir
        # determines if the sandbox should allow network access
        self.network_enabled = network_enabled

    @abstractmethod
    def run(self, command: str, stdin_path: str) -> dict:
        """
        Runs the command securely within the sandboxed environment.
        Returns a dict with 'stdout', 'stderr', and 'exit_code'.
        """
        pass
