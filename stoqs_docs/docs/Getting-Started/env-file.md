# Notes on the .env file

The `.env` file's location is: `/stoqs/.env`. This file provides all of the Docker containers with the environmental variables required for them to properly run and locate the necessary files. The `.env` file should be checked for system compatability  

## Important variables:

- `DEBUG`: This variable enables the debugpy functionality in the django. Which will pause execution each time `manage.py` is called until the vscode debuggers is connect. 
  - Set this variable to 1 to enable and any other value to disable
- `TEST`: This variable will force the server start script to execute `test.sh` which automatically runs unit tests.
  - Set this variable to 1 to enable or any other value to disable
- `GEOS_LIBRARY_PATH`: This variable defines the path to `libgeos_c.so`. The path will be different depending on the host machine's cpu architecture. The proper path should be uncommented and the other commented out.
  - Arm users should use `/usr/lib/aarch64-linux-gnu/libgeos_c.so`
  - x86 users should use `/usr/lib/x86_64-linux-gnu/libgeos_c.so`

## All Variables

| Variable Name | Description | Default | Note |
| :----------- | :--------- | :----- | :-- |
| `DEBUG` | Enables debugpy | 0 | set to 1 to enable |
| `TEST` | Forces unit test | 0 | set to 1 to force unit test |
| `GEOS_LIBRARY_PATH` | Path to `libgeos_c.so` | /usr/lib/x86_64-linux-gnu/libgeos_c.so | <comment \| uncomment\> per cpu |
| `STOQS_HOME` | Path on local machine to `/stoqs/` directory. Allows STOQS  to access files on local machine | x | This variable is disabled and `${PWD}` is used in the `local.yml` Windows users see [Windows Setup]() as this will not work |
| `STOQS_VOLS_DIR` | Temporary files such as the Postgres DB will be stored here on the local machine | `/tmp/docker_stoqs_vols` | This may need to be cleared see [Postgis Issues](../Known-Issues/Postgis-Issues.md) |
| `POSTGRES_DATA` | postgis db | `/tmp/docker_stoqs_vols/pgdata` | same as above |
| `POSTGRES_WALDIR` | maybe same as above? | `/tmp/docker_stoqs_vols/pg_waldir` | same as above? | 
| `PRODUCTION` | Should specify if we want to run in production mode | False | Not implemented | 
| `DJANGO_DEBUG` | ? | False | Not used. Leave false to reduce spam |
| `NGINX_TMPL` | nginx container not used | nginx.tmpl | unused |
| `UWSGI_READ_TIMEOUT` | server backend timeout | 300 | - |
| `STOQS_PGHOST` | Needed to connect to postgis | stoqs-postgis | just leave it as it |
| `STOQS_PGHOST_PORT` | Port postgis is listening on | 5432 | - |
| `POSTGRES_PASSWORD` | password to acces db | changeme | - |
| `STOQSADM_USER` | logs in to db during server run | stoqsadm | - |
| `STOQSADM_PASSWORD` | - | CHANGEME | - |
| `MAP_SERVER_NAME` | - | localhost | - |
| ` MAPFILE_DIR` | - | `/maps` | - |
