from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from movies.tasks import task_calculate_movie_ratings

User = get_user_model() # for custom auth

# Usage:
# (venv) PS D:\projects\recommender\src>
# python .\manage.py calculate_ratings
class Command(BaseCommand):

    # Adds arguments to the command.
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=1_000, type=int)
        parser.add_argument("--all", action='store_true', default=False)

    # Options: {'verbosity': 1, 'settings': None, 'pythonpath': None,
    #           'traceback': False, 'no_color': False,
    #           'force_color': False, 'skip_checks': False}
    def handle(self, *args, **options):
        all = options.get('all')
        count = options.get('count')
        task_calculate_movie_ratings(all=all, count=count)