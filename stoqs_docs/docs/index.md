# capstone_stoqs
CSUMB Otterbots capstone project.

![assets/images/Stoqs.png](assets/images/Stoqs.png)
### Description: 
> STOQS is a geospatial database and web application designed to give oceanographers efficient integrated access to in situ measurement and ex situ sample data. 

The objective of this project is to restructure the [stoqs system](https://github.com/stoqs/stoqs) to fit the [Django-cookiecutter](https://github.com/cookiecutter/cookiecutter-django) Template.

### Problem statement: 
- The current development version of STOQS is designed to run within a vagrant VM which makes it challenging to easily edit the code with a local IDE and see the changes refreshed live in the browse
- Django-cookiecutters use of docker containers sharing volumes with the local machine will hopefully make it easier for contributors to get started and make changes to STOQS

### Project Diagram

``` mermaid
flowchart LR
    Postgis[(Postgis)]
    Stoqs["Stoqs"]
    MapServer2["MapServer"]
    Postgis2[(Postgis)]
    Stoqs2["Stoqs"]
    MapServer2["MapServer"]

subgraph STOQS_Repo
    subgraph Host-Machine
        subgraph VirtualBox
            subgraph Vagrant
                subgraph CentOS-LinuxOS
                    Stoqs --> Postgis
                    Stoqs --> Mapserver
                end
            end
        end
    end
end
subgraph Capstone_Repo
    subgraph Host-Machine2
        subgraph Docker-STOQS
            Stoqs2
        end
        subgraph Docker-Postgis
            Postgis2
        end
        subgraph Docker-Mapserver
            MapServer2
        end
        Stoqs2 --> Postgis2
        Stoqs2 --> MapServer2
    end
end
STOQS_Repo --> Capstone_Repo
```
