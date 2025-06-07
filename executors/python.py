from generics.base_executor import BaseExecutor

class PythonExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        return f"python3 {self.code_file}"
