#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
>>>>>>> 0eecb15431dec5e5df18645314a36a1b6d964764
>>>>>>> eac57fad93156b3c93735af2440d0da1966a036c
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()