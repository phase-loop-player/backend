FROM python:3.6-slim
WORKDIR /app

COPY . .
RUN pip install gunicorn
RUN pip install -e ./

ENTRYPOINT [ "gunicorn" ]
