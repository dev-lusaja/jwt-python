bind = 'unix:/tmp/gunicorn.sock'
daemon = True
workers = 1
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'
reload = True
