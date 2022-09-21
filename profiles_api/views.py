from django.shortcuts import render
# Creating API View:
# uses http methods as functions i.e. get, post ..
# similar to django view -> where templates used, but here functions instead
# gives you the most control over application logic
# mapped manually to URLs

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TestApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns list of APIView features"""

        an_apiview = ['hello hi', 'hello bye']

        return Response({
            'message': 'test',
            'an_apiview': an_apiview
        })
