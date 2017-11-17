#!/bin/bash

/usr/sbin/nginx -g 'daemon off;' &
gunicorn server:api -b :9001 --reload --log-file=/var/log/uwsgi/uwsgi.log 2>>/var/log/uwsgi/uwsgi.log