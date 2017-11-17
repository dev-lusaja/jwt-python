#!/bin/bash

gunicorn -c /tmp/gunicorn.py server:api &
/usr/sbin/nginx -g 'daemon off;' &
tail -f /var/log/gunicorn/error.log /var/log/nginx/error.log