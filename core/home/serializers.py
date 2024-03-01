from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

   class Meta:
      model = Student
      #fields =['name','age']
      #exclude=['id,']
      field ='__all__'

      def validate(self, data):
         
         if data['age0']< 18:
            raise serializers.validationError({'error': "age cannot be less tha n 18"})
         if data['name']:
            for n in data['name']:
               if n.isdigit():
                   raise serializers.validationError({'error': "weight cannot be numeric "})
         
         return data