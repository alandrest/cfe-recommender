import random
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from movies.models import Movie
from .models import Rating, RatingChoice

User = get_user_model()

def generate_fake_reviews(count=10, users=10, null_avg=False):
    user_s = User.objects.first() # id=1
    user_e = User.objects.last()
    random_user_ids = random.sample(range(user_s.id, user_e.id), users)
    users = User.objects.filter(id__in=random_user_ids)
    # Other way to make it: users = User.objects.all().order_by("?")[:users]

    movies = Movie.objects.all().order_by("?")[:count]
    movie_ctype = ContentType.objects.get_for_model(Movie)
    if null_avg:
        movies = Movie.objects.filter(rating_avg__isnull=True).order_by("?")[:count]

    # One rating per movie itself
    n_ratings = movies.count()

    # We have nan values because of __empty__ option in the enum
    rating_choises = [x for x in RatingChoice.values if x is not None]
    user_ratings = [random.choice(rating_choises) for _ in range(0, n_ratings)]

    new_ratings = []
    for movie in movies:
        # Note 1:Single create instead of bulk to have different user and movie each time
        #        Otherwise if it is the same user and the same rating, the previous will be deleted.
        # Note2: we may use the save method but create is much more efficient.
        # Note3: one more method (the current one is not good enough as there are possible not enough "movies"
        #           -> ContentType
        rating_obj = Rating.objects.create(
            #content_object = movie,
            content_type=movie_ctype,
            object_id=movie.id,
            value=user_ratings.pop(),
            user=random.choice(users)
        )
        new_ratings.append(rating_obj.id)
    return new_ratings
