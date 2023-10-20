from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from cfehome import utils as cfehome_utils
from movies.models import Movie

User = get_user_model() # for custom auth


# Usage:
# python .\manage.py loader --movies

class Command(BaseCommand):

    # Adds arguments to the command.
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--movies", action='store_true', default=False)
        parser.add_argument("--users", action='store_true', default=False)
        parser.add_argument("--show-total", action='store_true', default=False)

    # Options: {'verbosity': 1, 'settings': None, 'pythonpath': None,
    #           'traceback': False, 'no_color': False,
    #           'force_color': False, 'skip_checks': False}
    def handle(self, *args, **options):
        # Get the arguments
        count = options.get('count')
        show_total = options.get('show_total')
        load_movies = options.get('movies')
        generate_users = options.get('users')

        # Movies
        if load_movies:
            movies_dataset = cfehome_utils.load_movie_data(limit=count)

            movies_new = [Movie(**x) for x in movies_dataset]
            movies_bulk = Movie.objects.bulk_create(movies_new, ignore_conflicts=True)

            print(f"New movies created: {len(movies_bulk)}.")
            if show_total:
                print(f"Overall Movies: {Movie.objects.count()}")

        # Profiles
        if generate_users:
            profiles = cfehome_utils.get_faked_profiles(count=count)

            new_users = []
            for profile in profiles:
                new_users.append(User(**profile))
            users_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)

            print(f"New users created: {len(users_bulk)}.")
            if show_total:
                print(f"Overall users: {User.objects.count()}")