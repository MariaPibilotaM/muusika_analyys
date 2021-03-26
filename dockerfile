FROM python:3.7
WORKDIR /app

RUN apt update && \
apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg wget git vim

COPY requirements.txt .
RUN pip install --upgrade pip && \
pip install -r requirements.txt

COPY /app .

CMD ["python3","app.py"]