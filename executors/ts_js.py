from generics.base_executor import BaseExecutor

class TSJSExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        if self.code_file.endswith(".ts"):
            return f"ts-node {self.code_file}"
        return f"node {self.code_file}"
