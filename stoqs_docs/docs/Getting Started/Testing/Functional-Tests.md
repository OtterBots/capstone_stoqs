## Running only functional tests (local-ci.yml)

In `.env` file, set `DEBUG=0` and `DJANGO_DEBUG=false`.  Stop any running containers.  This test will remove existing containers.  When the functional test is finished, you will need to re-create local.yml containers.

!!! Note
    This test uses Selenium, so use the following browser url: `http://localhost:7900/?autoconnect=1&resize=scale&password=secret`.  Selenium tests the stoqs website functionality, thus the pages will be automated.  There is no need to click anything in the browser while the test is running.

1. Open the terminal and go to the capstone_stoqs/stoqs directory where the local.yml is located.  Run the following command to remove all the containers:
    ```
    docker-compose -f local.yml down
    ```

2. Build `local-ci.yml` in detached mode:

    ```
    docker-compose -f local-ci.yml up -d --build
    ```

3. Run the `local-ci.yml`:
    ```
    export DATABASE_URL=postgis://stoqsadm:CHANGEME@stoqs-postgis:5432/stoqs
    ```

4. Start the functional test with the following command:
    ``` bash
    DATABASE_URL=$DATABASE_SUPERUSER_URL python manage.py test stoqs.tests.functional_tests --settings=config.settings.ci
    ```

5. Open browser to:
    ```
    http://localhost:7900/?autoconnect=1&resize=scale&password=secret
    ```

    Test takes over 5 minutes.

6. Container will stop when test is done.

7. Type `exit` in shell to exit.

!!! Note 
    When done with functional tests, you will need to remove the containers created by local-ci.yml (functional test containers) and re-create the local.yml development environment containers.
