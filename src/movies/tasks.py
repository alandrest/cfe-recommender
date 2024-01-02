from .models import Movie
from celery import shared_task
#
# @shared_task(name='task_calculate_movie_ratings')
# def task_calculate_movie_ratings(all=False, count=None):
#     '''
#     Usage:
#          # direct call from cli
#          task_calculate_movie_ratings(all=False, count=None)
#          # celery_config tasks:
#             task_calculate_movie_ratings.delay(all=False, count=None)
#             task_calculate_movie_ratings.apply_async(
#                                                      kwargs={"all": False,
#                                                              "count": 12},
#                                                      countdown=30) # delay from running for 30 secs
#                                                                    # other option: inside the function time.sleep(30)
#                                                     )
#     '''
#     qs = Movie.objects.needs_updating()
#
#     if all:
#         qs = Movie.objects.all()
#
#     # Older ones are first:
#     qs = qs.order_by('rating_last_updated')
#
#     if isinstance(count, int):
#         qs = qs[:count]
#
#     for obj in qs:
#         obj.calculate_rating(save=True)
#
# def task_calculate_movie_rating_all():
#     qs = Movie.objects.all()
#     for obj in qs:
#         obj.calculate_rating(save=True)
#
#
# def task_calculate_movie_rating_needs_updating():
#     qs = Movie.objects.needs_updating()
#     for obj in qs:
#         # row by row
#         # SQL -> Aggregate, Group
#         obj.calculate_rating(save=True)

# # Debug
# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     # from rating.models import Rating
#     # from django.contrib.auth import get_user_model
#     # User = get_user_model()
#     # rating_obj = Rating.objects.create(
#     #     content_object=Movie.objects.first(),
#     #     # content_type=movie_ctype,
#     #     # object_id=movie.id,
#     #     value=x+y,
#     #     user= User.objects.first()
#     # )
#     print("**********************************************")
#     print("              this is from the task           ")
#     print("**********************************************")
#     return x + y
