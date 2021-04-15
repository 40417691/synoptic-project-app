FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

COPY . /app

CMD ["python", "app.py"]