from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add gcc g++ make libffi-dev openssl-dev

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install flask flask-socketio PyVimeo==1.0.0 uwsgi -U flask-cors

EXPOSE 5000

ENTRYPOINT ["uwsgi"]
CMD ["http.ini"]

