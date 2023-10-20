from faker import Faker
import csv
from django.conf import settings
from pprint import pprint
import datetime

MOVIE_METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def validate_date_str(date_txt):
    try:
        datetime.datetime.strptime(date_txt, "%Y-%m-%d")
    except:
        return None
    return date_txt
def load_movie_data(limit=10):
    with open(MOVIE_METADATA_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = []
        for i, row in enumerate(reader):

            _id = row.get('id')
            try:
                _id = int(_id)
            except:
                _id = None

            release_date = validate_date_str(row.get("release_date"))

            data = {"id": _id,
                    "title": row.get("title"),
                    "overview": row.get("overview"),
                    "release_date": release_date
                    }
            dataset.append(data)

            if i + 1 > limit:
                break
        return dataset

def get_faked_profiles(count=10):
    fake = Faker()
    user_data = []
    for _ in range(count):
        profile = fake.profile()
        data = {"username": profile.get('username'),
                "email": profile.get('mail'),
                #"password": make_password(fake.password(length=15)),
                "is_active": True,
                }
        if 'name' in profile:
            fname, lname = profile.get('name').split(" ")[:2]
            data['first_name'] = fname
            data['last_name'] = lname
        user_data.append(data)
    return user_data


