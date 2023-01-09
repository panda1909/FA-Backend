from django.contrib import admin
from .models import Links, MenuItems, Manifesto, FeaturedClients, ContactUs, PopUp

# Register your models here.
admin.site.register(Links)
admin.site.register(MenuItems)
admin.site.register(Manifesto)
admin.site.register(FeaturedClients)
admin.site.register(ContactUs)
admin.site.register(PopUp)
