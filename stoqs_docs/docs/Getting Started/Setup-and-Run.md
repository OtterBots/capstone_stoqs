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
11. Windows users beware! Also M1 users :apple: