#!/usr/bin/env bash

python manage.py makemigrations;
python manage.py migrate;
exec python manage.py runserver;
