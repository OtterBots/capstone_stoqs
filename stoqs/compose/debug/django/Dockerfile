FROM osgeo/gdal:ubuntu-small-3.6.0

# Depreciated
# MAINTAINER Mike McCann <mccann@mbari.org>

ENV PYTHONUNBUFERED=1

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Inlined FROM pcic/geospatial-python
RUN apt-get update && \
    apt-get -yq install \
    libgdal-dev \
    libyaml-dev \
    lsb-core \
    wget \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Need at least pip 22.1 for --root-user-action option below
RUN pip install -U pip

#IS this dangerous?
RUN pip install "setuptools<58.0.0"

# Needed so that postgresql-client is version 15
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc > /etc/apt/trusted.gpg.d/pgdg.asc

# Additional requirements for stoqs
RUN apt-get update && \
    apt-get -yq install \
    freetds-dev \
    git \
    # Install here rather than from .devcontainer/devcontainer.json
    git less wget zsh ssh-client \
    gmt \
    graphviz \
    graphviz-dev \
    locales \
    # Required by chromedriver: https://stackoverflow.com/a/65107381/1281657
    libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev \
    # Required for google-chrome-stable - https://askubuntu.com/a/79284
    libxss1 libappindicator1 libindicator7 \
    libxml2-dev \
    libxslt-dev \
    libgeos-dev \
    python3-dev \
    postgresql-client \
    time \
    xvfb \
    && locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# To fix multiprocessing-permission-denied for docker-compose execution
RUN echo 'none /dev/shm tmpfs rw,nosuid,nodev,noexec 0 0' > /etc/fstab

# Make sure python and python-config refer to corresponding Python 3 versions
RUN cd /usr/bin/ &&\
    ln -fs python3.10 python && \
    ln -fs python3.10-config python-config

WORKDIR /srv

# Symlink to requirements from docker directory used to minimize context
COPY requirements /requirements
RUN /bin/bash -c 'pip install -r /requirements/local.txt --root-user-action=ignore'

# Install ChromeDriver for Selenium
RUN curl -L -o /usr/local/bin/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip \
  && unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin

# Install Google Chrome - https://askubuntu.com/a/79284
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt-get update && apt-get install -y ./google-chrome*.deb

# Connection to uwsgi/nginx
COPY compose/local/stoqs/docker-stoqs-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# For functional tests and running development/debug/ci
COPY compose/local/stoqs/stoqs-start-run_server.sh /
RUN chmod +x /stoqs-start-run_server.sh
COPY compose/local/stoqs/stoqs-start.sh /stoqs-start.sh


# Make the script executable
RUN chmod +x /stoqs-start.sh

# Change the CMD to execute the stoqs-start.sh script

CMD ["compose/local/stoqs/stoqs-start.sh"]
