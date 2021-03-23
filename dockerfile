FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt-get install --no-cache libav-tools


COPY /app .

CMD ["python","app.py"]