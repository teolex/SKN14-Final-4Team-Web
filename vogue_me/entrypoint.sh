#!/bin/bash

python manage.py collectstatic --noinput
exec gunicorn -c gunicorn.conf.py
