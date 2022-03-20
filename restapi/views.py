from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class MainView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'password': 1212121
        }
        return Response(data)
