FROM python:3.8

RUN apt-get update
RUN apt-get install iputils-ping curl -y
COPY ./src/ /src/
RUN pip install -r /src/requirements.txt

ENTRYPOINT ["bash", "-c", "/src/entrypoint.sh"]
