# ARM vs x86 Compatibility

## MapServer
Currently the MapServer container is unable to start on ARM machines the only logs ouput are:
```
starting fcgiwrap 
Fail!
Exit code 1
```
This is still under investigation with no path to resolution
> Potential workaround found. Found another mapserver image on dockerhub that is tagged with arm64. Comment out and uncomment the lines as necessary in `Dockerfile-mapserver`

``` yaml linenums="1" 
#FROM mapserver/mapserver:v7.4.2
FROM camptocamp/mapserver:542-arm64
USER root

# Installing the build dependencies
RUN apt-get update -y && apt-get install -y libfcgi-dev fcgiwrap nginx

```

## STOQS
One of the stoqs dependencies is a package called libgeos which when installed on an arm host (Apple M1-2) will install into an `aarch64` directory as opposed to the `x86` directory when built on an x86 host. 

- Refer to `.env` file. Uncomment and comment the paths based on your system

``` bash linenums="90"
# Library locations as provided in base image for Dockerfile-stoqs
GEOS_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgeos_c.so
#GEOS_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/libgeos_c.so
```

A more graceful approach to this is likely possible but for now, here we are.
