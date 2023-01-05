from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os

from .models import Links, MenuItems, Manifesto, FeaturedClients, PopUp
from .serializers import LinksSerializer, MenuItemsSerializer, ManifestoSerializer, FeaturedClientsSerializer, \
    ContactUsSerializer, PopUpSerializer

from datetime import datetime


class LinksAPI(APIView):

    def get(self, request):
        get_links = Links.objects.all()
        serializer = LinksSerializer(get_links, many=True)

        return Response(serializer.data)


class MenuItemsAPI(APIView):

    def get(self, request):
        menu_items = MenuItems.objects.all()
        serializer = MenuItemsSerializer(menu_items, many=True)
        print(serializer.data)
        return Response(serializer.data)


class ManifestoAPI(APIView):

    def get(self, request):
        get_manifesto = Manifesto.objects.all()
        serializer = ManifestoSerializer(get_manifesto, many=True)
        return Response(serializer.data)


class FeaturedClientsAPI(APIView):

    def get(self, request):
        featured_clients = FeaturedClients.objects.all()
        serializer = FeaturedClientsSerializer(featured_clients, many=True)
        return Response(serializer.data)


class ContactUsAPI(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopUpAPI(APIView):

    def get(self):
        today = datetime.today()
        if PopUp.objects.filter(from_date__lte=today.date(), to_date__gte=today.date()).exists():
            pop_up = PopUp.objects.filter(from_date__lte=today.date(), to_date__gte=today.date()).first()
        else:
            pop_up = PopUp.objects.latest('id')

        serializer = PopUpSerializer(pop_up)
        return Response(serializer.data)


class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()
