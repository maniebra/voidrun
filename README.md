# VoidRun: An Isolated Environment for Code Execution

## About the Project

VoidRun is an isolated environment for code execution. It provides a safe and secure environment for executing code in a controlled environment, preventing potential vulnerabilities or attacks. It uses Firejail, a sandboxing tool, to isolate the code execution environment, ensuring that the code is executed in a controlled and secure environment.

## Usecases

Examples of usecases for VoidRun include:


- Testing code in a controlled environment.
- Debugging code in a controlled environment.
- Executing code in a controlled environment.
- Juging code in a controlled environment.

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
sudo apt-get install firejail
pip install voidrun
```

Or in an Arch based distro:

```bash
sudo pacman -S firejail
pip install voidrun
```


