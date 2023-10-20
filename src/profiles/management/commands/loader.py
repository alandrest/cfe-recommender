from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from cfehome import utils as cfehome_utils

User = get_user_model() # for custom auth

class Command(BaseCommand):

    # Adds arguments to the command.
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--show-total", action='store_true', default=False)

    # Options: {'verbosity': 1, 'settings': None, 'pythonpath': None,
    #           'traceback': False, 'no_color': False,
    #           'force_color': False, 'skip_checks': False}
    def handle(self, *args, **options):
        count = options.get('count')
        show_total = options.get('show_total')

        profiles = cfehome_utils.get_faked_profiles(count=count)

        new_users = []
        for profile in profiles:
            new_users.append(User(**profile))

        users_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)

        print(f"New users created: {len(users_bulk)}.")
        if show_total:
            print(f"Overall users: {User.objects.count()}")