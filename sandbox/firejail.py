import subprocess
import os
from generics.base_sandbox import BaseSandbox

class FirejailSandbox(BaseSandbox):
    def __init__(
        self,
        working_dir: str,
        timeout: int = 5,
        max_processes: int = 10
    ):
        super().__init__(working_dir)
        self.timeout = timeout
        self.max_processes = max_processes

    def run(self, command: str, stdin_path: str) -> dict:
        # Wrap the user command with ulimit + firejail + timeout
        sandbox_cmd = (
            f"ulimit -u {self.max_processes}; "
            f"firejail --quiet --net=none --private={self.working_dir} "
            f"timeout {self.timeout} {command}"
        )

        try:
            result = subprocess.run(
                ["bash", "-c", sandbox_cmd],
                cwd=self.working_dir,
                stdin=open(os.path.join(self.working_dir, stdin_path), "r"),
                capture_output=True,
                text=True,
                timeout=self.timeout + 2  # buffer for wrapper timeout
            )

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": "Execution timed out.",
                "exit_code": 124
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": f"Internal error: {str(e)}",
                "exit_code": 1
            }
