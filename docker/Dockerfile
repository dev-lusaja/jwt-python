FROM amazonlinux:latest

MAINTAINER Oscar Sanchez <dev-lusaja>

# Install Python, tools and Nginx

RUN yum -y update \
    && yum -y install python27 python27-pip \
    && yum -y install nginx

ADD resources /tmp/
RUN pip install -r /tmp/requirement.txt
RUN /tmp/setconfigs.sh

EXPOSE 80
WORKDIR /app
ENTRYPOINT /tmp/runservices.sh