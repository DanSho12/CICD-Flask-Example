FROM alpine:latest

RUN apk update && apk add \
    python3 \
    py3-pip

RUN pip3 install Flask gunicorn

WORKDIR /app
COPY ./web/*.py /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
