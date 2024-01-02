import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome')

# CELERY_, the namespace as the  const variable first part at the settings.py
app.config_from_object("django.conf:settings", namespace='CELERY')
# one more option: use instead (if not using Django):
# app.conf.broker_url = ''
# app.conf.result_backend='django-db'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # "generate_fake_review_every_1_min": {
    #     'task': 'generate_fake_reviews',
    #     'schedule': 1 * 60,  # 1 min
    #     'kwargs': {"count": 1_000}
    # },

    # "run_movie_rating_avg_every_30":{
    #     'task': 'task_update_movie_ratings',
    #     'schedule': 30 * 60, # 30 mins
    #     'kwargs': {"count": 1000}
    # },
    # "add-every-30": {
    #     'task': 'sum_two_numbers',
    #     'schedule': 30,
    #     'kwargs': {"x": 6, "y": 7}
    # }
    #
    # celery -A cfehome worker -l info
    "run_movie_rating_avg_every_30_mins":{
        # this is the name from D:\projects\recommender\src\movies\tasks.py, "@shared_task('task_calculate_movie_ratings')"
        # if we would define it as: "@shared_task" then it should've been ike this:
        # 'task': 'movies.tasks.task_calculate_movie_ratings'
        'task': 'task_calculate_movie_ratings',

        # 30 mins = 30*60 secs
        'schedule': 30 * 60,

        'kwargs': {"all": True}
    },

    # the same name as defined at the @shared_task, see \src\exports\tasks.py
    "export_rating_dataset_every_1_hour": {
        'task': 'export_rating_dataset',
        'schedule': 60 * 60,  # 1 hour
    },

}