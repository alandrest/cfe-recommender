from .models import RatingChoice

def get_rating_choices(request):
    return {
        "rating_choices": RatingChoice.values
    }