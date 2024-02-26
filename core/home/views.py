from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 
# Create your views here.
@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()
    return Response({'status': 200,'payload':"hello"})

@api_view(['POST'])
def post_Student(request):
   data =request.data
   serializer= StudentSerializer(data=request.POST)
   return Response({'status': 200,'payload': data, 'message': 'you ar worthy of eveerrything'})