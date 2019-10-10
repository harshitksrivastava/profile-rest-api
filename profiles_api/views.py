from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """ Returns a list of APIViews features """
        an_apiview = [
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]
        # the dict in Response() it will be converted to JSON so it needs to be dict or list
        return Response({'message':'Hello!','an_apiview': an_apiview})
