from generics.base_executor import BaseExecutor

class CExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        # Compilation + run (all inside sandbox working dir)
        return f"gcc {self.code_file} -o a.out && ./a.out"
