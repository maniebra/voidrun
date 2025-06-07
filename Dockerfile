FROM debian:bookworm-slim

RUN apt update && apt install -y \
    python3 python3-pip \
    firejail gcc g++ \
    nodejs npm \
    curl coreutils \
    && npm install -g ts-node \
    && pip install fastapi uvicorn python-multipart

WORKDIR /app
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
