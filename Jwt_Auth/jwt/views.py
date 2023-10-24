from django.shortcuts import render
from rest_framework import viewsets
from  . models import Student
from .serializer import StudentSerializer
from jwt.custom_auth import CustomeAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class StudentModelViewApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    