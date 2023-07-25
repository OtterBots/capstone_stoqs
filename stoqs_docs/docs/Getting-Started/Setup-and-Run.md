## Installation from terminal (for base cookiecutter-django project)

View [cookie_config.txt](../../../cookie_config.txt) file for settings used.

1. Clone repo (your ssh should already be setup):
```git clone git@github.com:OtterBots/capstone_stoqs.git```
2. Change directory to the directory which contains `local.yml`:From the root of the project -> `cd stoqs`
3. Edit the `stoqs/.env`: change the `STOQS_HOME` variable to be the absolute path to the dockeer-compose file (check with `pwd` from the STOQS home directory)
4. in local.yml the last volume in the stoqs service has been changed from `${STOQS_HOME}` to `${PWD}` to mount the directory that local.yml is run from to `/srv/` this works well on unix/linux machines. Change it back to `${STOQS_HOME}` if you want to use the fully qualified hardcoded path mentioned in step 3
``` yaml hl_lines="6" linenums="16"
    volumes:
      - ${STOQS_VOLS_DIR}/maps:${MAPFILE_DIR}
      - ${STOQS_VOLS_DIR}/stoqs_root:/root
      - ${STOQS_VOLS_DIR}/nginx:/usr/share/nginx
      - ${STOQS_VOLS_DIR}/pg_dumps:/srv/media-files/pg_dumps
      - ${PWD}:/srv
      - static-files:/srv/static-files
      - media-files:/srv/media-files
```
7. Make sure your Docker Desktop program is running.
8. Build project:
```docker-compose -f local.yml build```
9. Run project:
```docker-compose -f local.yml up```
10. View project in browser:
`localhost:8000/stoqs`
11. Windows users beware! Also M1 users :apple:
