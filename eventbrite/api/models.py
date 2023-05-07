from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from front_end.models import User


#creating user model by importing get_user_model from django
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# A DB table is been created for events:
class Event(models.Model):
    user = models.ForeignKey(User,related_name='events',on_delete=models.CASCADE)
    name = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(default='')
    image = models.ImageField(upload_to='event_picture/',blank=True)
    likes = models.ManyToManyField(User,through='EventLikes')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('api:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']
        unique_together = ['user','name']

#A DB table for likedevents by the user:
class EventLikes(models.Model):
    event = models.ForeignKey(Event,related_name='event_likes',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_likes',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('event','user')
