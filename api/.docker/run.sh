#!/bin/bash
if [[ $ENV == 'docker' ]]; then
	# docker (local)
	python manage.py migrate && python manage.py runserver 0.0.0.0:8000
else
	# deploy
	cp /usr/src/app/nginx.conf /etc/nginx/sites-available/default
	cp /usr/src/app/supervisor.conf /etc/supervisor/conf.d/
	supervisord -n
fi
