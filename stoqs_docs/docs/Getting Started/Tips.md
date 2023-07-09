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