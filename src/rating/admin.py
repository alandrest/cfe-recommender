from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = ['user'] # search in separate window
    readonly_fields = ['content_object']

admin.site.register(Rating, RatingAdmin)