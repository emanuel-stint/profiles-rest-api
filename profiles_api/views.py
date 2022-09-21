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
        return Response({
            'method': 'PUT'
        })

    # This is a partial udpate -> i.e. only update the fields that were included in the request, everything else stays the same
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
