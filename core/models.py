from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Links(TimeStamp):
    link = models.URLField(max_length=1024)
    name = models.CharField(max_length=256)


class MenuItems(TimeStamp):
    link = models.URLField(max_length=1024)
    image = models.FileField(upload_to='nav_items/')


class Manifesto(TimeStamp):
    video = models.FileField(upload_to='manifesto/')
    content = models.TextField()


class FeaturedClients(TimeStamp):
    name = models.CharField(max_length=512)
    logo = models.FileField(upload_to='featured_clients/')
