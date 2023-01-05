from django.urls import path
from .views import LinksAPI, MenuItemsAPI, ManifestoAPI, FeaturedClientsAPI, ContactUsAPI, PopUpAPI

from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', LinksAPI.as_view(), name='links'),
    path('menu-items', MenuItemsAPI.as_view(), name='menu-items'),
    path('manifesto', ManifestoAPI.as_view(), name='manifesto'),
    path('featured-clients', FeaturedClientsAPI.as_view(), name='featured-clients'),
    path('contact-us', ContactUsAPI.as_view(), name='contact-us'),
    path('pop-up', PopUpAPI.as_view(), name='pop-up'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)