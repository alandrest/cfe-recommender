from .models import RatingChoice

# This gnna be rendered on every single template, be carefull not to make it too heavy (prefer not to fetch it from the db).
def get_rating_choices(request):
    return {
        # this is the key used in template: {{ rating choises }}
        "rating_choices": RatingChoice.values # choices: [(k, val)]
    }