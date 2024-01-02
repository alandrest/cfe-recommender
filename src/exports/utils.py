from rating.models import Rating
from django.db.models import F
from django.contrib.contenttypes.models import ContentType
import csv
import tempfile
from django.apps import apps
from django.core.files.base import File

# Usage: df = pd.DataFrame(generate_movie_rating_dataset())
def generate_movie_rating_dataset(app_label='movies', model='movie'):
    ctype = ContentType.objects.get(app_label=app_label, model=model)
    qs = Rating.objects.filter(active=True, content_type=ctype)
    qs = qs.annotate(userId=F('user_id'), movieId=F('object_id'), rating=F('value'))
    return qs.values('userId', 'movieId', 'rating')

def export_dataset(app_label='movies', model='movie'):
    Export = apps.get_model('exports', 'Export')

    # Create the temp file
    with tempfile.NamedTemporaryFile(mode='r+') as temp_f:
        dataset = generate_movie_rating_dataset(app_label=app_label, model=model)
        try:
            keys = dataset[0].keys()
        except:
            return
        dict_writer =csv.DictWriter(temp_f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataset)
        temp_f.seek(0) # go to the top of the file

        # write the Export model
        obj = Export.objects.create()
        obj.export_file.save("export.csv", File(temp_f))