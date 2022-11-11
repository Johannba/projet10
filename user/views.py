from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import UserSignupSerializer

# Create your views here.
User = get_user_model()


class SignupViewset(APIView):

    """
    Create User. Return 201 code if successfully created
    """

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)