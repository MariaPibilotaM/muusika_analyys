FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt update
RUN apt-get install libav-tools && \
apt-get install -y python-scipy\
python-numpy python-pandas &&\
apt-get clean && rm -rf /var/lib/apt/lists/*


COPY /app .

CMD ["python3","app.py"]