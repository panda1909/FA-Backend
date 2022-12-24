from rest_framework import serializers
from .models import Links, MenuItems, Manifesto, FeaturedClients, ContactUs

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'
        

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['link', 'image']

class ManifestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifesto
        fields = ['video', 'content']

class FeaturedClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedClients
        fields = ['name', 'logo']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'