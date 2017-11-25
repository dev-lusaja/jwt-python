#!/bin/bash

/usr/sbin/nginx -g 'daemon off;' &
gunicorn -c /tmp/gunicorn.py server:api
