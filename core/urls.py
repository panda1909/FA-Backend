from django.urls import path
from .views import Links, MenuItems, Manifesto, FeaturedClients, ContactUs

app_name = 'core'

urlpatterns = [
    path('', Links.as_view(), name='links'),
    path('menu-items', MenuItems.as_view(), name='menu-items'),
    path('manifesto', Manifesto.as_view(), name='manifesto'),
    path('featured-clients', FeaturedClients.as_view(), name='featured-clients'),
    path('contact-us', ContactUs.as_view(), name='contact-us'),
]