from django.shortcuts import render
from rest_framework import generics
from .serializers import ScheduleSerializer
from .models import Schedule
# Create your views here.



class ListSchedules(generics.ListAPIView):
    serializer_class=ScheduleSerializer
    queryset=Schedule.objects.all()



schedules=ListSchedules.as_view()
