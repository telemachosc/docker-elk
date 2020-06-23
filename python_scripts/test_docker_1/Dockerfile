FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /test_docker_1
WORKDIR /test_docker_1
COPY . /test_docker_1

CMD python ./test_1.py