from generics.base_executor import BaseExecutor

class PythonExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        # first file is treated as the entry point
        main_file = self.code_files[0]
        return f"python3 {main_file}"
