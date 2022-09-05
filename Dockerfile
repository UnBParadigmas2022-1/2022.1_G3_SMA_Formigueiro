FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip & \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8521

COPY entrypoint.sh /usr/bin
RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]

