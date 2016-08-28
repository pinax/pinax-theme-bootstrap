import errno
import glob
import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand


def copy(src, dest):
    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            dest="path",
            help="a glob wildcard to copy templates from"
        )

    def handle(self, *args, **options):
        path = options["path"]
        base = os.path.join(os.path.dirname(__file__), "../../templates")
        dest = os.path.join(settings.PACKAGE_ROOT, "templates")
        for f in glob.glob(os.path.join(base, path)):
            print(f.replace(base, dest))
            copy(f, f.replace(base, dest))
