```
.
├── cookie_config.txt
├── README.md
└── stoqs
    ├── compose
    │   ├── local
    │   │   ├── django
    │   │   │   ├── Dockerfile
    │   │   │   └── start
    │   │   └── docs
    │   │       ├── Dockerfile
    │   │       └── start
    │   └── production
    │       ├── django
    │       │   ├── Dockerfile
    │       │   ├── entrypoint
    │       │   └── start
    │       ├── nginx
    │       │   ├── default.conf
    │       │   └── Dockerfile
    │       ├── postgres
    │       │   ├── Dockerfile
    │       │   └── maintenance
    │       │       ├── backup
    │       │       ├── backups
    │       │       ├── restore
    │       │       └── _sourced
    │       │           ├── constants.sh
    │       │           ├── countdown.sh
    │       │           ├── messages.sh
    │       │           └── yes_no.sh
    │       └── traefik
    │           ├── Dockerfile
    │           └── traefik.yml
    ├── config
    │   ├── api_router.py
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── base.py
    │   │   ├── __init__.py
    │   │   ├── local.py
    │   │   ├── production.py
    │   │   └── test.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── CONTRIBUTORS.txt
    ├── COPYING
    ├── docs
    │   ├── conf.py
    │   ├── howto.rst
    │   ├── index.rst
    │   ├── __init__.py
    │   ├── make.bat
    │   ├── Makefile
    │   └── users.rst
    ├── LICENSE
    ├── locale
    │   ├── en_US
    │   │   └── LC_MESSAGES
    │   │       └── django.po
    │   ├── pt_BR
    │   │   └── LC_MESSAGES
    │   │       └── django.po
    │   └── README.md
    ├── local.yml
    ├── manage.py
    ├── merge_production_dotenvs_in_dotenv.py
    ├── production.yml
    ├── pyproject.toml
    ├── README.md
    ├── requirements
    │   ├── base.txt
    │   ├── local.txt
    │   └── production.txt
    ├── setup.cfg
    ├── stoqs
    │   ├── conftest.py
    │   ├── contrib
    │   │   ├── __init__.py
    │   │   └── sites
    │   │       ├── __init__.py
    │   │       └── migrations
    │   │           ├── 0001_initial.py
    │   │           ├── 0002_alter_domain_unique.py
    │   │           ├── 0003_set_site_domain_and_name.py
    │   │           ├── 0004_alter_options_ordering_domain.py
    │   │           └── __init__.py
    │   ├── __init__.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── project.css
    │   │   ├── fonts
    │   │   ├── images
    │   │   │   └── favicons
    │   │   │       └── favicon.ico
    │   │   └── js
    │   │       └── project.js
    │   ├── templates
    │   │   ├── 403.html
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   ├── account
    │   │   │   ├── account_inactive.html
    │   │   │   ├── base.html
    │   │   │   ├── email_confirm.html
    │   │   │   ├── email.html
    │   │   │   ├── login.html
    │   │   │   ├── logout.html
    │   │   │   ├── password_change.html
    │   │   │   ├── password_reset_done.html
    │   │   │   ├── password_reset_from_key_done.html
    │   │   │   ├── password_reset_from_key.html
    │   │   │   ├── password_reset.html
    │   │   │   ├── password_set.html
    │   │   │   ├── signup_closed.html
    │   │   │   ├── signup.html
    │   │   │   ├── verification_sent.html
    │   │   │   └── verified_email_required.html
    │   │   ├── base.html
    │   │   ├── pages
    │   │   │   ├── about.html
    │   │   │   └── home.html
    │   │   └── users
    │   │       ├── user_detail.html
    │   │       └── user_form.html
    │   ├── users
    │   │   ├── adapters.py
    │   │   ├── admin.py
    │   │   ├── api
    │   │   │   ├── serializers.py
    │   │   │   └── views.py
    │   │   ├── apps.py
    │   │   ├── context_processors.py
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests
    │   │   │   ├── factories.py
    │   │   │   ├── __init__.py
    │   │   │   ├── test_admin.py
    │   │   │   ├── test_drf_urls.py
    │   │   │   ├── test_drf_views.py
    │   │   │   ├── test_forms.py
    │   │   │   ├── test_models.py
    │   │   │   ├── test_swagger.py
    │   │   │   ├── test_urls.py
    │   │   │   └── test_views.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   └── utils
    │       ├── __init__.py
    │       └── storages.py
    └── tests
        └── test_merge_production_dotenvs_in_dotenv.py
```
