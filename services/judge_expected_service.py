from services.run_script import run_code_and_capture


def judge_expected(
    lang: str,
    code_files,
    stdin_file,
    expected_output: str,
    setup_commands=None,
    network_enabled: bool = False,
) -> dict:
    result = run_code_and_capture(
        lang,
        code_files,
        stdin_file,
        setup_commands=setup_commands,
        network_enabled=network_enabled,
    )
    result["correct"] = result["stdout"].strip() == expected_output.strip()
    return result
