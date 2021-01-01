# DjangoMango Core

## Setup

#### Dependencies:

* Install docker (20.10.0+) & docker-compose (1.27.4+)
	* e.g. for Ubuntu, see: https://docs.docker.com/engine/install/ubuntu/
	
* Note, to upgrade docker-compose to the latest version (if installed via curl):

```
sudo rm /usr/local/bin/docker-compose
COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
sudo curl -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```


#### To run locally for development:

* Build and run via docker-compose:

```
docker-compose -f docker-compose.dev.yml --env-file dev.env up
```

* Browse to 127.0.0.1:8000


#### To run for production (without ssl):

* Build and run via docker-compose:

```
docker-compose -f docker-compose.prod.yml --env-file prod.env up
```


#### To run for production (with ssl):

* Build and run via docker-compose:

```
docker-compose -f docker-compose.prod.ssl.yml --env-file prod.env up
```


#### To pull core data for the application:

* bash into the web container ID (docker ps && docker exec -it [id] bash), and run the following manage.py commands:

```
python manage.py run_rebuild_core
```


## Useful Commands

* Django commands --

```
# delete migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete &&
find . -path "*/migrations/*.pyc"  -delete

# make migrations
python manage.py makemigrations --noinput &&
python manage.py migrate --noinput
```

* web management commands --

```
# restart gunicorn
kill -SIGHUP [pid]

# note that docker spawns CMD as init pid 1, so to restart gunicorn within docker
docker exec [container_id] kill -SIGHUP 1
```

* Docker commands ---

```
# show all running docker images
docker ps

# run command within image
docker exec [container_id] [command]

# bash into image
docker exec -it [container_id] bash

# copy file from host to image
docker cp [source_file_path] [container_id]:[dest_file_path]

# follow logs from an image
docker logs [container_id] -f

# follow logs from docker-compose
docker-compose -f [config.yml] logs -f

# drop all docker images/volumes etc.
docker stop $(docker ps -qa); docker rm $(docker ps -qa); docker rmi -f $(docker images -qa); docker volume rm $(docker volume ls -q); docker network rm $(docker network ls -q)
```