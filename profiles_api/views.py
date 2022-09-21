from django.shortcuts import render
# Creating API View:
# uses http methods as functions i.e. get, post ..
# similar to django view -> where templates used, but here functions instead
# gives you the most control over application logic
# mapped manually to URLs

from rest_framework.views import APIView
from rest_framework.response import Response
# Used to determine responses from api -> status codes
from rest_framework import status
# Creating viewsets
from rest_framework import viewsets

from profiles_api import serializers


# Create your views here.


class TestApiView(APIView):
    """Test API View"""

    # Tells api view what data to expect when making http requests to api
    # Class is accessible to all
    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        """Returns list of APIView features"""

        an_apiview = ['hello hi', 'hello bye']

        return Response({
            'message': 'test',
            'an_apiview': an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""

        # standrard way to retrieve serializer and assigns the data
        serializer = self.serializer_class(data=request.data)

        # validating serializer -> this ensures that name entry was in fact char of lenght 5
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        # if there is an issue with the serizaler
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            # Simply pass issues with serializer and also the right status code - not 200!

    # Usually when doing a put / patch -> you would do it to a pk: primary key, as the update is associated with a spcific object
    def put(self, request, pk=None):
        """Handle updating object, completely"""
        return Response({
            'method': 'PUT'
        })

    # This is a partial udpate -> i.e. only update the fields that were included in the request, everything else stays the same
    def patch(self, request, pk=None):
        """Handle partially updating object, with fields included in request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting a particular object"""
        return Response({'method': 'DELETE'})


class TestViewSet(viewsets.ViewSet):
    """Test API viewset"""

    # Uses actions -> list, create, retrieve, update, partial_update
    # Automaticallys maps urls using 'Routers'
    # Provides more functionality with less code

    serializer_class = serializers.TestSerializer

    def list(self, request):
        """Reurn a hello message"""
        a_viewset = [
            'Hello hi'
        ]

        return Response({'message': 'hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Fetch info about particular object"""
        return Response({'method': 'RETRIEVE'})

    def update(self, request, pk=None):
        """Update particular object completely"""
        return Response({'method': 'UPDATE'})

    def partially_update(self, request, pk=None):
        """Partially update object with fields included in request"""
        return Response({'method': 'PARTIALLY_UPDATE'})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DESTROY'})
