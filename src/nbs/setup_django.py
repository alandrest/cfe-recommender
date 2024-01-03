"""
Instead of this, run in the first cell of the notebook:

import os, sys
import django
PROJECTPATH = 'D:\\projects\\recommender\\src'
sys.path.insert(0, PROJECTPATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cfehome.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # https://docs.djangoproject.com/en/4.1/topics/async/#async-safety
os.chdir(PROJECTPATH)
django.setup()

"""
import os
import sys

DJANGO_SETTINGS_MODULE = "cfehome.settings"

# PWD = os.getenv("PWD")
from pathlib import Path
PWD = Path(__file__).resolve().parent.parent

def init():
    print(PWD, type(PWD))
    os.chdir(str(PWD))
    sys.path.insert(0, os.getenv("PWD"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()
