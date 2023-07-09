# Tips

### Python debug messsages (stoqs container)
By default print line statements in python files will not be printed to docker logs or the console. In order to get print statements for debugging purposes change we need to set the environment variable `PYTHONUNBUFFERED` to 

1. This can be done in the Dockerfile-stoqs. After enabling rebuild the containers with `docker-compose -f local.yml build`

``` yaml linenums="1" hl_lines="7"
FROM osgeo/gdal:ubuntu-small-3.6.0

# Depreciated
# MAINTAINER Mike McCann <mccann@mbari.org>

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
```
---

### Quickly destroy all containers and images
- Destroy containers:

``` 
docker rm $(docker ps -a | cut -d' ' -f1 | grep -v CONTAINER | xargs) 
```

- Destroy images:

```
docker rmi $(docker images | awk {'print $3'} | grep -v IMAGE | xargs)
```
---
### Postgres and datagrip or any data munging software for that matter
- The port of the postgress container is exposed in the local.yml file allowing you to connect to the database from localhost:5432 to explore the db.
    - Default username and password are defined in `.env` current settings are:
        - Name: stoqsadm
        - Pw:   CHANGEME

``` yaml linenums="61" hl_lines="3"
command: postgres -c config_file=/etc/postgresql.conf
ports:
  - "${STOQS_PGHOST_PORT}:5432"
# Set user for deployment on MacOS, assign HOST_UID=<result of `id -u`> in your .env file
# user: ${HOST_UID}
```