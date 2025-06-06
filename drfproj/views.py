# drfapp/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drfapp.models import Student
from drfapp.serializers import StudentSerializer

class TesView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
