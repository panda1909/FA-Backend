from rest_framework import serializers
from .models import Links, MenuItems, Manifesto, FeaturedClients, ContactUs

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'

class ManifestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifesto
        fields = '__all__'

class FeaturedClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedClients
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'