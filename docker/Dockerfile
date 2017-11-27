FROM amazonlinux:latest

MAINTAINER Oscar Sanchez <dev-lusaja>

# Install Python, tools and Nginx

RUN yum -y update \
    && yum -y install python27 python27-pip \
    && yum -y install nginx

ADD resources /tmp/
RUN pip install -r /tmp/requirement.txt
RUN /tmp/setconfigs.sh

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80
WORKDIR /app
ENTRYPOINT /tmp/runservices.sh