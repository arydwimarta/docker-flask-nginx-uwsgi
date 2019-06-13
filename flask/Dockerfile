#use python3.7.2 container image
FROM python:3.7.2-stretch

#set working directory
WORKDIR /app

#copy current directory into container
ADD . /app

#install dependencies
RUN pip install -r requirements.txt

#run the command to start uWSGI
CMD ["uwsgi", "app.ini"]