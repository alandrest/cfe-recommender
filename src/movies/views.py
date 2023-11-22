from django.shortcuts import render
from django.views import generic
from .models import Movie
from rating.models import Rating

class MovieListView(generic.ListView):
    template_name = 'movies/list.html'
    paginate_by = 100
    # context -> object_list
    queryset = Movie.objects.all().order_by('-rating_avg')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context['object_list'])
        request = self.request
        user = request.user
        if user.is_authenticated:
            object_list = context['object_list']
            object_ids = [x.id for x in object_list][:20]
            #my_ratings =  user.rating_set.movies().as_object_dict(object_ids=object_ids)
            my_ratings_objs = Rating.objects.filter(object_id__in=object_ids).filter(active=True, content_type=7) # filter active movies
            my_ratings = {x.id: x.value for x in my_ratings_objs}
            context['my_ratings'] = {f"{x.object_id}": f"{x.value}" for x in my_ratings_objs}


        return context

#     # Instead of addint "rating_choises" to the context with render at the func my_view
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         print(context)
#         # context['rating_choises'] = RatingChoise.values
#         return context
#
movie_list_view = MovieListView.as_view()

# 3 ways to do the same (Add rating_choisesto the context):
# 1. func get_context_data to use Django
# 2. adding rating_choises hardcoded when render
# 3. setting.TEMPLATES contains it
#    in the template html: {{ rating_choises }} (see movies/snippet/card.html)
#    ratings/context_processors.py:
class MovieDetailView(generic.DetailView):
    template_name = 'movies/detail.html'
    # context -> object -> id
    queryset = Movie.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        user = request.user
        if user.is_authenticated:
            object = context['object']
            object_ids = [object.id]
            #my_ratings = user.rating_set.movies().as_object_dict(object_ids=object_ids)
            my_ratings_objs = Rating.objects.filter(object_id__in=object_ids).filter(active=True, content_type=7)  # filter active movies
            my_ratings = {x.id: x.value for x in my_ratings_objs}

            context['my_ratings'] = my_ratings
        return context

movie_detail_view = MovieDetailView.as_view()