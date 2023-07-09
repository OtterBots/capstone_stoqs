# Postgis issues

1. On startup postgis displays error logs which state an invalid password, ownership issues, or non empty db
```
error: directory "/var/lib/postgresql/data/db_files" exists but is not empty
```
2. No data is being loaded into the database on startup and there is no data currently stored in the database

---
Refer to the postgis service in local.yml and the `${POSTGRES_DATA}` varbiale in the `.env` file. The Postgis container mounts the database data in a directory which is located on the local machine. As such, the data stored in it will persist through container restarts and even rebuilds. If the container is rebuilt, for some reason it occasionally loses access to db data. Additionally, If the `test.sh` script has run on the database and failed to load data, the database will have been created and subsequent container starts will not attempt to load data. 
- For both of scenarios, it can be corrected by wiping out the temporary data. If your have used the default POSTGRES variables in the .env files, the temmporary data can be removed with `rm -rf /tmp/docker_stoqs_vols` This is a safe action and the containers will recreate the needed directories on next startup.
```yaml linenums="52"
  postgis:
    image: mbari/stoqs-postgis
    build:
      context: .
      dockerfile: ./compose/production/postgres/Dockerfile-postgis
    volumes:
      - ${POSTGRES_DATA}:/var/lib/postgresql/data
      - ${POSTGRES_WALDIR}:/var/lib/postgresql/waldir
      - ./compose/production/postgres/postgres15-stoqs.conf:/etc/postgresql.conf
```
``` bash linenums="25"
# POSTGRES_DATA and POSTGRES_WALDIR: Locations for the permanent database files
# - Main data files and write ahead log variables exist for putting on separate volumes
#   On production and development servers change to a more permanent location
POSTGRES_DATA=/tmp/docker_stoqs_vols/pgdata
POSTGRES_WALDIR=/tmp/docker_stoqs_vols/pg_waldir

```
