FROM amazonlinux:latest

MAINTAINER Oscar Sanchez <dev-lusaja>

# Install Python, tools and Nginx

RUN yum -y update \
    && yum -y install python27 python27-pip \
    && yum -y install nginx

ADD config /tmp/config
RUN pip install -r /tmp/config/requirement.txt

WORKDIR /app
EXPOSE 9001
CMD gunicorn app:api -b :9001 --reload