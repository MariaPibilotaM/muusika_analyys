FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt update
RUN apt-get install libav-tools


COPY /app .

CMD ["python3","app.py"]