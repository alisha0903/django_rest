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
   serializer= StudentSerializer(data=request.data)

   if request.data['age']<18:
       return Response({'status':403, 'message':'age must be greater than 18'})
   if not serializer.is_valid():
       return Response({'status': 403, 'message':'something went wrong'})
   
   serializer.save()
   
   return Response({'status': 200,'payload': serializer.data, 'message': 'you are worthy of eveerrything'})

@api_view(['PUT'])
def update_Student(request):
   try:
     student_obj=Student.objects.get(id=id)

     serializer= StudentSerializer(student_obj,data=request.data, partial=true)

     if request.data['age']<18:
       return Response({'status':403, 'message':'age must be greater than 18'})
     if not serializer.is_valid():
       return Response({'status': 403, 'message':'something went wrong'})
   
     serializer.save()
   
     return Response({'status': 200,'payload': serializer.data, 'message': 'you are worthy of eveerrything'})
   except Exception as e:
      return Response({'status':403,'message':'invalid id'})