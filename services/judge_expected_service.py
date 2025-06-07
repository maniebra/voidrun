from services.run_script import run_code_and_capture

def judge_expected(lang: str, code_file, stdin_file, expected_output: str) -> dict:
    result = run_code_and_capture(lang, code_file, stdin_file)
    result["correct"] = result["stdout"].strip() == expected_output.strip()
    return result
