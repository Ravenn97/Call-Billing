FROM python:3.7-alpine3.9

LABEL  MAINTAINER="Tung Do <tungdv97@gmail.com>"
RUN apk update
RUN apk add gcc musl-dev python3-dev

RUN pip3 install cython
RUN pip3 install --upgrade pip
COPY requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

COPY ./ /var/www/
WORKDIR /var/www/




