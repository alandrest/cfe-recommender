from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from .models import Rating
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def rate_movie_view(request):
  if not request.htmx:
      return HttpResponse("Not Allowed", status=400)

  object_id = request.POST.get('object_id')
  rating_value = request.POST.get('rating_value')

  if object_id is None or rating_value is None:
      # may be makes sense to log it that people do skip it a lot.
      response = HttpResponse("Skipping", status=200)

      # this is the trigger name which we could use somewhere else
      # here: will use it for refreshing the outer html (itself):
      # (see templates/movies/snippet/infinite.html)
      response['HX-Trigger'] = 'did-skip-movie'

      return response

  user=request.user
  message = "You must <a href='accounts/login/'>login</a> to rate this."

  if user.is_authenticated:
      message = "<div class='bg-danger text-light py-1 px-3 rounded'>An error occured</div>"
      ctype = ContentType.objects.get(app_label='movies', model='movie')
      rating_obj = Rating.objects.create(content_type=ctype,
                                         object_id=object_id,
                                         value=rating_value,
                                         user=user)
      if rating_obj.content_object is not None:
          message = "<div class='bg-success text-light py-1 px-3 rounded'>Rating saved</div>"
          response = HttpResponse(message, status=200)

          # this is the trigger name which we will use for refreshing to other (random) movie after the settle
          # (see templates/movies/snippet/infinite.html)
          response['HX-Trigger-After-Settle'] = 'did-rate-movie'
          return response

  return HttpResponse(message, status=200)
