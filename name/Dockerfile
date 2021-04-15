FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

#matches the port in py file
EXPOSE 5001 

COPY . /app

CMD ["python", "namesvc.py" ]