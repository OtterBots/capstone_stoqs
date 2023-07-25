## Installation from terminal (first time)

1. Clone repo (your ssh should already be setup):
    ```
    git clone git@github.com:OtterBots/capstone_stoqs.git
    ```

2. Change directory to the stoqs project folder which contains `local.yml`:
    ```
    cd capstone_stoqs/stoqs
    ```

3. Edit the `.env` file depending if your processor is x86 (intel/amd) or arm64 (apple silicon):
    ```
    # Library locations as provided in base image for Dockerfile-stoqs
    # This path will vary depending on your architecture use aarch64 for arm (apple silicon) and use x86 for intel/amd.
    # GEOS_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/libgeos_c.so
    GEOS_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgeos_c.so
    ```

4. Edit the `Dockerfile-mapserver` file located at `compose/local/mapserver` depending on whether you are x86 or arm64:
    ```
    # Change this variable based on your cpu. Use arm64 for arm (apple silscon)
    FROM mapserver/mapserver:v7.4.2
    # FROM camptocamp/mapserver:8.0-arm64
    ```

5. Edit settings in `.env` (optional) (0: off, 1: on):
    ```
    ## This variable enables debugpy listener in manage.py
    DEBUG=0

    ## This variable forces start-stoqs.sh to run test.sh set TEST=1 to run test.sh
    TEST=0
    ```

6. Make sure your Docker Desktop program is running.  (Should be installed for your particular system.)

7. Build project:
    ```
    docker-compose -f local.yml build
    ```

8. Run project:
    ```
    docker-compose -f local.yml up
    ```

9. View project in browser: ```localhost:8000/stoqs```

10. To exit:
    ```
    docker-compose -f local.yml stop
    ```
    or stop containers using Docker Desktop.

!!! Note
    All runs after only require that step 8 and onward, unless changes were made to build files or changes to .env settings.


# Troubleshooting

1. Windows OS pathing issues and other operating system dependant complications.

    Guide coming soon.

2. asdf

    more stuff soon


!!! Info
    View [cookie_config.txt](../../../cookie_config.txt) file for settings used in this project.
