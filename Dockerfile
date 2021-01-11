FROM ubuntu:latest
LABEL "MAINTAINER"="saidsalihefendic@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /qa
WORKDIR /qa
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "qa/app.py" ]