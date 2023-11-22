from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import Avg
from django.db.models.signals import post_save
from django.utils import timezone
from django.apps import apps

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

# class RatingQuerySet(models.QuerySet):
#     def avg(self):
#         return self.aggregate(average=Avg('value'))['average'] # creates dict: {"average": 1.2}
#
#     def movies(self):
#         Movie = apps.get_model('movies', 'Movie')
#         ctype = ContentType.objects.get_for_model(Movie)
#         return self.filter(active=True, content_type=ctype)
#
#     def as_object_dict(self, object_ids=None):
#         if object_ids is not None:
#             qs = self.filter(object_id__in=object_ids)
#         else:
#             qs = self.all()
#
#         return {f"{x.object_id}": x.value for x in qs}
#
# class RatingManager(models.Manager):
#     def get_queryset(self):
#         return RatingQuerySet(self.model, using=self._db)
#
#     def movies(self):
#         return self.get_queryset().movies()
#
#     def avg(self):
#         return self.get_queryset().avg()

class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True, choices=RatingChoice.choices)

    # Basic implementation of the Generic Foreign Key:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() # this will not w ork if my id is UUIDField as my primary key
    content_object =GenericForeignKey("content_type", "object_id")

    active = models.BooleanField(default=True)
    active_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    #objects = RatingManager() # so we could do: Rating.objects.avg(), Rating.objects.all().avg()

    class Meta:
        ordering = ['-timestamp']

# To prevent the same user+movie, both Rating's active.
# Other way: after the creation to look for all the duplicates and to handle them.
# But in production the best practice is: post signal (below) or override the save method.
def rating_post_save(sender, instance, created, *args, **kwargs):
    if created:
        _id = instance.id
        if instance.active:
            qs = Rating.objects.filter(content_type=instance.content_type,
                                       object_id=instance.object_id,
                                       user=instance.user
                                       ).exclude(id=_id, active=True)
            if qs.exists():
                # Update only those whose timestamp is not set yet
                qs = qs.exclude(active_update_timestamp__isnull=False)

                # Other decision: qs.delete()
                # We are not deleting as we want the user's activity about changing their mind.
                qs.update(active=False,
                          active_update_timestamp=timezone.now()
                          )

post_save.connect(rating_post_save, sender=Rating)
