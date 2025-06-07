FROM debian:bookworm-slim

RUN apt update && apt install -y \
    python3 python3-pip \
    firejail gcc g++ \
    nodejs npm \
    curl coreutils


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt 
RUN pip install -r requirements.txt --break-system-packages
RUN npm install -g ts-node

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
