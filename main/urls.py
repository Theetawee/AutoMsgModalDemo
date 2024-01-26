from django.urls import path
from .views import schedules


urlpatterns=[
    path('',schedules)
]
