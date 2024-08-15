FROM python:3.9-slim

RUN pip install numpy

COPY . /app
WORKDIR /app

CMD ["python", "genetic_algorithm.py"]
