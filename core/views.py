from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Links, MenuItems, Manifesto, FeaturedClients, ContactUs
from .serializers import LinksSerializer, MenuItemsSerializer, ManifestoSerializer, FeaturedClientsSerializer, ContactUsSerializer


class Links(APIView):

    def get(self, request):
        links = Links.objects.all()
        serializer = LinksSerializer(links, many=True)
        return Response(serializer.data)

class MenuItems(APIView):

    def get(self, request):
        menu_items = MenuItems.objects.all()
        serializer = MenuItemsSerializer(menu_items, many=True)
        return Response(serializer.data)

class Manifesto(APIView):

    def get(self, request):
        manifesto = Manifesto.objects.all()
        serializer = ManifestoSerializer(manifesto, many=True)
        return Response(serializer.data)

class FeaturedClients(APIView):

    def get(self, request):
        featured_clients = FeaturedClients.objects.all()
        serializer = FeaturedClientsSerializer(featured_clients, many=True)
        return Response(serializer.data)

class ContactUs(APIView):

    def post(self, request, *args, **kwargs):
        data = {
                'name': request.data.get('name'), 
                'company': request.data.get('company'), 
                'email': request.data.get('email'), 
                'subject': request.data.get('subject'), 
                'message': request.data.get('message'), 
            }
        serializer = ContactUsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        contact_us = ContactUs.objects.all()
        serializer = ContactUsSerializer(contact_us, many=True)
        return Response(serializer.data)