# capstone_stoqs
CSUMB Otterbots capstone project.

### Description: goes here.

### Problem statement: 
- Update docker containers for local development envirionment of stoqs with postgresql server.
- Refactor STOQS to conform to cookiecutter Django file structure
- Improve system resources
  #### Before:
- Docker Images
```
mbari/stoqs-mapserver          latest    fc4a219a5447   58 seconds ago   1.21GB
mbari/stoqs                    latest    59dfcf2c38cc   9 minutes ago    3.38GB
mbari/stoqs-nginx              latest    bf389e963ed6   5 days ago       109MB
mbari/stoqs-postgis            latest    e9795be56070   3 weeks ago      625MB
```
- Docker Containers Running

```
CONTAINER ID   NAME              CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O        PIDS
35a43162cc1d   stoqs-postgis     0.02%     18.64MiB / 13.51GiB   0.13%     3.87kB / 1.57kB   1.37MB / 4.1kB   7
f21150c3e557   stoqs-mapserver   0.00%     15.84MiB / 13.51GiB   0.11%     2.48kB / 0B       496kB / 0B       19
8c402c7ec86c   stoqs             100.18%   11.34MiB / 13.51GiB   0.08%     3.75kB / 1.43kB   10.8MB / 0B      3
0df1fce8e2bf   stoqs-nginx       0.00%     2.645MiB / 13.51GiB   0.02%     2.18kB / 0B       57.3kB / 0B      3
```

Objective:

---

## Installation from terminal (for base cookiecutter-django project)

View [cookie_config.txt](cookie_config.txt) file for settings used.

1. Clone repo (your ssh should already be setup):
```git clone git@github.com:OtterBots/capstone_stoqs.git```
2. Change to project directory:
```cd stoqs```
3. copy or rename `template.env` to `.env`
4. change the `STOQS_HOME` variable to be the absolute path to the dockeer-compose file (check with `pwd` from the STOQS home directory)
5. place `.env` in STOQS home (same directory as docker-compose.yml)
6. This doenst work yet but we would like it to
7. Make sure your Docker Desktop program is running.
8. Build project:
```docker-compose -f local.yml build```
9. Run project:
```docker-compose -f local.yml up```
10. View project in browser:
```http://127.0.0.1:8000```
or
```localhost:8000```
You should now see the default project page.

---

# Work Flow

1. Make a local branch
2. blah blah blah
3. Push to your own branch.
4. When ready, do pull request to the dev branch.
** drew I need help with the instructions.

