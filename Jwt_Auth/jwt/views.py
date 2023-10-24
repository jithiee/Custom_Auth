from django.shortcuts import render
from rest_framework import viewsets
from  . models import Student
from .serializer import StudentSerializer
from jwt.custom_auth import CustomeAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentModelViewApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomeAuthentication]
    permission_classes = [IsAuthenticated]
    
    