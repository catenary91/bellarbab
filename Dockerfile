FROM python:3.12.2-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt ./
RUN ["python", "-m", "pip", "install", "--upgrade", "pip"]
RUN ["pip",  "install", "-r", "requirements.txt"]

COPY . .

EXPOSE 80/tcp
VOLUME ["/app/database"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:6060"]