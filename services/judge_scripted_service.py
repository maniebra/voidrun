from services.run_script import run_code_and_capture

def judge_with_script(lang: str, code_file, stdin_file, judge_script_path: str) -> dict:
    result = run_code_and_capture(lang, code_file, stdin_file)
    try:
        import subprocess
        judge_result = subprocess.run(
            ["bash", judge_script_path],
            input=result["stdout"],
            capture_output=True,
            text=True,
            timeout=5
        )
        result["script_stdout"] = judge_result.stdout
        result["script_stderr"] = judge_result.stderr
        result["correct"] = judge_result.returncode == 0
    except Exception as e:
        result["script_error"] = str(e)
        result["correct"] = False
    return result
