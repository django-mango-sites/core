# pull web app image
FROM python:3.9.0-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create dirs
RUN mkdir /home/app
RUN mkdir /home/app/logs
RUN mkdir /home/app/staticfiles

# copy all to app dir
COPY . /home/app/

# set app as work dir
WORKDIR /home/app/

# update env
RUN apt-get update

# install and update pip
RUN pip install --upgrade pip

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# make wait-for-it.sh executable
RUN chmod +x wait-for-it.sh