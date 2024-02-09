FROM python:3.10.12-alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001/tcp
VOLUME ["/app/database"]

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "bellarbab.wsgi:application"]