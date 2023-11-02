FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-k", "eventlet", "-w", "1", "-b", "0.0.0.0:5001", "run:create_app()"]
