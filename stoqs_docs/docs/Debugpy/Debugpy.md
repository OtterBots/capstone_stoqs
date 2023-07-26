# Running DebugPy

The debugger, debugpy, is implemented in a containerized Django project to enable remote debugging via Visual Studio Code (VS Code). By setting up a run configuration to attach to the Docker container and modifying the manage.py file to include debugpy, developers gain the ability to set breakpoints, inspect variables, and step through code during execution. This debugging process enhances issue identification and resolution, providing valuable insights into the application's behavior within the containerized environment.

#To debug the Stoqs application using Debugpy, follow these steps:

Make sure you are in the "capstone_stoqs/stoqs" directory in the terminal:

1. Change directory to the first "stoqs" directory `cd capstone_stoqs/stoqs`
2. In the `.env` file ensure `DEBUG` environemental variable is set to 1 
2. Build Containers:  `docker-compose -f local.yml build`

3. Open vscode from the stoqs directory. `code .`

  !!! note
  The top level directory in vscode needs to be `capstone_stoqs/stoqs` for debugpy to work. This is because we need to map this directory to the `/srv` directory in the container and vscode looks for the `.vscode/launch.json` file in the top level

5. Start container stack: `docker-compose -f local.yml up`
Open Visual Studio Code (VSCode) and make sure the launch.json configuration is present.

6. Attach the debugger in VSCode:
    * Look for the "Run and Debug" panel in VSCode.
    * Select the "Python: Django" configuration.
    * Click the "Start Debugging" button.
    * The application will start building, and the debugger will prompt for attachment.

Follow any further prompts during the build process, if required.

# Issues Encountered:

>Running with launch.json and Django Python: Ensure that you have the Python extension installed in VSCode and that the launch configuration points to the correct paths of your Django project and manage.py file.

>Container Compatibility: Debugging a Django application within a Docker container may sometimes reveal issues related to container compatibility and configurations. Ensure that the Docker images and containers are set up correctly, with appropriate volumes and environment variables for the debugger to function seamlessly.







