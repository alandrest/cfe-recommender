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
    "run_movie_rating_avg_every_30":{
        'task': 'task_update_movie_ratings',
        'schedule': 30 * 60, # 30 mins
    },
    # "add-every-30": {
    #     'task': 'sum_two_numbers',
    #     'schedule': 30,
    #     'kwargs': {"x": 6, "y": 7}
    # }
    #
    # celery -A cfehome worker -l info
    # "run_movie_rating_avg_every_30_mins":{
    #     # this is the name form D:\projects\recommender\src\movies\tasks.py, "@shared_task('task_calculate_movie_ratings')"
    #     # if we would define it as: "@shared_task" then it should've been ike this:
    #     # 'task': 'movies.tasks.task_calculate_movie_ratings'
    #     'task': 'task_calculate_movie_ratings',
    #
    #     # 30 mins = 30*60 secs
    #     'schedule': 30 * 60,
    #
    #     'kwargs': {"all": True}
    # }
}