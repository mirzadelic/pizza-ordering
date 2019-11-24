FROM python:3.7-slim

RUN apt-get update --fix-missing

WORKDIR /usr/src/app/

ENV DJANGO_SETTINGS_MODULE=api.settings.docker
ADD . /usr/src/app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

RUN bash -c "chmod +x ./.docker/run.sh"
CMD ["./.docker/run.sh"]
