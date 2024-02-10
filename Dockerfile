FROM python:3.10.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt ./
RUN ["pip",  "install", "-r", "requirements.txt"]

COPY . .

EXPOSE 80/tcp
VOLUME ["/app/database"]

CMD ["gunicorn", "--bind", "0.0.0.0:80", "bellarbab.wsgi:application"]