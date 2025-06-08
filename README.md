# VoidRun: An Isolated Environment for Code Execution

## About the Project

VoidRun is an isolated environment for code execution. It provides a safe and secure environment for executing code in a controlled environment, preventing potential vulnerabilities or attacks. It uses Firejail, a sandboxing tool, to isolate the code execution environment, ensuring that the code is executed in a controlled and secure environment.

## Usecases

Examples of usecases for VoidRun include:


- Testing code in a controlled environment.
- Debugging code in a controlled environment.
- Executing code in a controlled environment.
- Judging code in a controlled environment.
- Running projects that require installing dependencies or network access.

## New Features

- **Multi-file execution**: upload several files at once.
- **Dependency installation**: provide setup commands like `pip install`.
- **Optional networking**: enable network access when needed for tests.

## Installation

### Docker

You can use VoidRun with Docker:

```bash
docker pull maniebra/voidrun:latest
```

### Linux (Manual)

Install Firejail and VoidRun using the following commands (i.e. in a terminal in a debian based distro):

```bash
sudo apt-get update
sudo apt-get install -y \
    python3 python3-pip \
    firejail gcc g++ \
    nodejs npm \
    curl coreutils

npm install -g ts-node
pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000
```
