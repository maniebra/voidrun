from generics.base_executor import BaseExecutor

class TSJSExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        main_file = self.code_files[0]
        if main_file.endswith(".ts"):
            return f"ts-node {main_file}"
        return f"node {main_file}"
