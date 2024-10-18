
FROM python:3.9-slim

WORKDIR /app

COPY src/requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY src/ /app

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
