#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Add parent folder to path so that we can import Minipub itself.
    PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])
    sys.path.append(os.path.join(PROJECT_PATH, ".."))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_project.settings")
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
    execute_from_command_line(sys.argv)
