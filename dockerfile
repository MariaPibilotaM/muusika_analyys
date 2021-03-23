FROM alpine
FROM python:3.7
WORKDIR /app

RUN apt update
RUN apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg wget git vim
RUN apt-get install python3.7

COPY requirements.txt .
RUN pip install --upgrade pip && \
pip install -r requirements.txt

COPY /app .

CMD ["python3","app.py"]