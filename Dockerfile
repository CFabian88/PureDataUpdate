FROM python:3.7.3
RUN apt-get update\
  && apt-get install expect -y
RUN apt-get -y install git
ADD . /pure-data-update
WORKDIR /pure-data-update
RUN pip install -r requirements.txt