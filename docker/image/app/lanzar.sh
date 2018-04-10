#!/bin/bash
#if [ -f .firstTime ]; then
#   echo "Creando configuracion inicial.."
#   rm .firstTime
#   python manage.py migrate
#   #python manage.py createsuperuser --username test1 --password 123321 --noinput --email 'blank@email.com'
#fi
python manage.py runserver 0.0.0.0:8000 &
