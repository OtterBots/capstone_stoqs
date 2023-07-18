#!/usr/bin/env python
import os
import sys
import debugpy
from pathlib import Path

## DEBUGPY
from django.conf import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

     # This allows easy placement of apps within the interior
    # stoqs directory.
    current_path = Path(__file__).resolve()
    sys.path.append(str(current_path / "stoqs"))
    print('arg1: {}'.format(sys.argv[1]))
    ####### ADDDING DEBUGPY ########
    # $ This will only activate the debugger when runserver arg is passed. Uncomment to run debugger all the time

    if settings.DEBUG and not os.getenv("RUN_MAIN") and os.getenv("DEBUG") == '1':
        debugpy.listen(("0.0.0.0", 3000))
    ## BLOCK EXECUTION AND WAIT FOR DEBUGGER uncomment if you want it to wait for you to connect vscod
        print('Awaiting debugger')
        debugpy.wait_for_client()
        print('Attached!')

    ## END DEBUGPY INSERT

    execute_from_command_line(sys.argv)