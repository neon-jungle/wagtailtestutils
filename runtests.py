#!/usr/bin/env python
import sys
import os
import warnings

from django.core.management import execute_from_command_line


os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


def runtests():
    # Don't ignore DeprecationWarnings
    warnings.simplefilter('default', DeprecationWarning)
    warnings.simplefilter('default', PendingDeprecationWarning)

    # Don't ignore ResourceWarnings (Python 3 only)
    if sys.version_info >= (3, 0):
        warnings.simplefilter('default', ResourceWarning)

    argv = sys.argv[:1] + ['test'] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
