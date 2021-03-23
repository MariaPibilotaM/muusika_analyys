FROM python:3.7
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt update
RUN apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg wget git vim

COPY /app .

CMD ["python3","app.py"]