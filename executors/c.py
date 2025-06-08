from generics.base_executor import BaseExecutor

class CExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        # Compilation with potentially multiple files then execution
        sources = " ".join(self.code_files)
        return f"gcc {sources} -o a.out && ./a.out"
