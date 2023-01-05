import datetime
from django.utils import timezone

from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Links(TimeStamp):
    link = models.URLField(max_length=1024)
    name = models.CharField(max_length=256)

    blank = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Link'


class MenuItems(TimeStamp):
    link = models.URLField(max_length=1024)
    image = models.FileField(upload_to='nav_items/')

    blank = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'


class Manifesto(TimeStamp):
    video = models.FileField(upload_to='manifesto/')
    content = models.TextField()

    class Meta:
        verbose_name = 'Manifesto'
        verbose_name_plural = 'Manifesto'


class FeaturedClients(TimeStamp):
    name = models.CharField(max_length=512)
    logo = models.FileField(upload_to='featured_clients/')

    class Meta:
        verbose_name = 'Featured Client'
        verbose_name_plural = 'Featured Clients'


class ContactUs(TimeStamp):
    name = models.CharField(max_length=1024)
    company = models.CharField(max_length=1024)
    email = models.EmailField()
    subject = models.CharField(max_length=1024)
    message = models.TextField()

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'


class PopUp(TimeStamp):
    link = models.URLField(max_length=1024)
    image = models.FileField(upload_to='pop_up/')
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)

    blank = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'PopUp'
        verbose_name_plural = 'PopUps'
