from generics.base_executor import BaseExecutor

class CPPExecutor(BaseExecutor):
    def get_execution_command(self) -> str:
        return f"g++ {self.code_file} -o a.out && ./a.out"
