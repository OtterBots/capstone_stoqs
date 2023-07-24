# Running DebugPy

The debugger, debugpy, is implemented in a containerized Django project to enable remote debugging via Visual Studio Code (VS Code). By setting up a run configuration to attach to the Docker container and modifying the manage.py file to include debugpy, developers gain the ability to set breakpoints, inspect variables, and step through code during execution. This debugging process enhances issue identification and resolution, providing valuable insights into the application's behavior within the containerized environment.

#To debug the Stoqs application using Debugpy, follow these steps:

Make sure you are in the "capstone_stoqs/stoqs" directory in the terminal:

`cd capstone_stoqs/stoqs`
Build the Docker containers:

`docker-compose -f local.yml build`
Start the application and wait for the prompt to attach the debugger in the Terminal:

`docker-compose -f local.yml up`
Open Visual Studio Code (VSCode) and make sure the launch.json configuration is present.

Attach the debugger in VSCode:

Look for the "Run and Debug" panel in VSCode.
Select the "Python: Django" configuration.
Click the "Start Debugging" button.
The application will start building, and the debugger will prompt for attachment.

Follow any further prompts during the build process, if required.

# Issues Encountered:

>Running with launch.json and Django Python: Ensure that you have the Python extension installed in VSCode and that the launch configuration points to the correct paths of your Django project and manage.py file.

>Container Compatibility: Debugging a Django application within a Docker container may sometimes reveal issues related to container compatibility and configurations. Ensure that the Docker images and containers are set up correctly, with appropriate volumes and environment variables for the debugger to function seamlessly.







