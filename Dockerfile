FROM python:3.6-slim-buster
WORKDIR /app

COPY . .
RUN apt-get update -y && apt-get install -y ffmpeg
RUN pip install gunicorn
RUN pip install -e ./

ENTRYPOINT [ "gunicorn" ]
