from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    #tells post and update to what data to expect
    serializer_class = serializers.HelloSerializer

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

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else :
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':"PUT"})

    def patch(self,request,pk=None):
        """Handles a partial update of an object"""
        return Response({'method':"PATCH"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_viewset = [
        'uses actions (list,create,retrieve,update,partial_update)',
        'automatically maps to urls using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    def retrieve(self,request,pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        """ Handle updating part of an object """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})
