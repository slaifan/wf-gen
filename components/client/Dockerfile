FROM python:3.8

USER root
# RUN commands

RUN apt-get update
RUN apt-get install -y python3 python3-pip iputils-ping curl 

# COPY ./src/ /src/

RUN pip install --upgrade pip && pip install -r /src/requirements.txt

USER 1001


ENTRYPOINT ["bash", "-c", "/src/entrypoint.sh"]
