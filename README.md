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
mbari/stoqs-mapserver          latest    fc4a219a5447   58 seconds ago   1.21GB
mbari/stoqs                    latest    59dfcf2c38cc   9 minutes ago    3.38GB
mbari/stoqs-nginx              latest    bf389e963ed6   5 days ago       109MB
mbari/stoqs-postgis            latest    e9795be56070   3 weeks ago      625MB
```

Objective:

---

## Installation from terminal (for base cookiecutter-django project)

View [cookie_config.txt](cookie_config.txt) file for settings used.

1. Clone repo (your ssh should already be setup):
```git clone git@github.com:OtterBots/capstone_stoqs.git```
2. Change to project directory:
```cd stoqs```
3. Make sure your Docker Desktop program is running.
4. Build project:
```docker-compose -f local.yml build```
5. Run project:
```docker-compose -f local.yml up```
6. View project in browser:
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

