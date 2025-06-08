# Installation

## Docker

You can use VoidRun with Docker:

```bash
docker pull maniebra/voidrun:latest
```

## Linux (Manual)

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
