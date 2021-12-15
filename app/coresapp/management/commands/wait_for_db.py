import time

from django.db import connections  # use to test if the db connection is available
from django.db.utils import OperationalError  # operational error that django will throw if the db is not available
from django.core.management.base import \
    BaseCommand  # class that we need to build on in order to create custom command class


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("waiting for database.....")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']

            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
