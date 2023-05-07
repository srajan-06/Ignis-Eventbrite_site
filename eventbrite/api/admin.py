from django.contrib import admin
from . import models

# Registering models:
class EventLikesInline(admin.TabularInline):
    model = models.EventLikes

admin.site.register(models.Event)
