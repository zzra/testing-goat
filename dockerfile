FROM python:slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src /src

WORKDIR /src

RUN python manage.py collectstatic
RUN python manage.py migrate

#CMD gunicorn --bind :8888 superlists.wsgi:application --forwarded-allow-ips "*"
CMD gunicorn --bind :8888 superlists.wsgi:application --forwarded-allow-ips "*" 