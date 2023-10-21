from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from rating.tasks import generate_fake_reviews
from rating.models import Rating

User = get_user_model() # for custom auth

# Usage:
# (venv) PS D:\projects\recommender\src>
# python .\manage.py fake_ratings 1000 --users 500 --show-total
class Command(BaseCommand):

    # Adds arguments to the command.
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--show-total", action='store_true', default=False)
        parser.add_argument("--users", default=1000, type=int)

    # Options: {'verbosity': 1, 'settings': None, 'pythonpath': None,
    #           'traceback': False, 'no_color': False,
    #           'force_color': False, 'skip_checks': False}
    def handle(self, *args, **options):
        # Get the arguments
        count = options.get('count')
        show_total = options.get('show_total')
        user_count = options.get('users')

        new_ratings = generate_fake_reviews(count=count, users=user_count)
        print(f'New ratings: {len(new_ratings)}')

        if show_total:
            print(f'Overall ratings: {Rating.objects.all().count()}')