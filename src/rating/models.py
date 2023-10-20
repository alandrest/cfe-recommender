from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = settings.AUTH_USER_MODEL # 'auth.User'

# user_obj = User.objects.first()
# user_ratings = user_obj.rating_set.all()
#
# rating_obj = Rating.objects.first()
# user_obj = rating_obj.user
# user_ratings = user_obj.rating_set.all()

# Here: Generic Foreign key

class RatingChoice(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    __empty__ = "Rate this"

class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True, choices=RatingChoice.choices)

    # Basic implementation of the Generic Foreign Key:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() # this will not w ork if my id is UUIDField as my primary key
    content_object =GenericForeignKey("content_type", "object_id")

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)


