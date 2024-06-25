FROM python:3.8.9

COPY . /web

WORKDIR /web

RUN pip install --no-cache -r requirements.txt

EXPOSE 8080

ENTRYPOINT python3 -B main.py