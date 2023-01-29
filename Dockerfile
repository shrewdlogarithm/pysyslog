FROM python:3.9.1
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

VOLUME /app/data

CMD ["python", "pysyslog.py"]