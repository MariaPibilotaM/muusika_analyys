FROM ubuntu:20.10
FROM python:3.7
WORKDIR /app

RUN apt-get update
RUN apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg wget git vim

RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD ["python3","app.py"]