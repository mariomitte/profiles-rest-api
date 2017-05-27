# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# POST metoda = uključuje serializers
from . import serializers
from rest_framework import status

# Django viewset
from rest_framework import viewsets


# Django rest_framework API response
class HelloApiView(APIView):
    """Test API View."""

    # dodaj serializers varijablu i referenciraj ju
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    # metoda za POST response
    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data) # što god da request ima pošalji serializer objektu

        # provjeri da serializer ima ispravni data
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name) # {0, 1, 2} to je red po kojemu želim izlistati message koji je upisao korisnik
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST) # sadrži lista grešaka koji nastanu

    # Http response
    def put (self, request, pk=None):
        """Handles updating object."""

        return Response({'method': 'put'})

    # Partialy update object
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object."""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test APi ViewSet."""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
