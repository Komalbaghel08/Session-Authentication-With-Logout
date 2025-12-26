from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.
from rest_framework.authentication import  BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated  

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    permission_classes = [IsAuthenticated]
  
    queryset = Student.objects.all()
    serializer_class =StudentSerializer 