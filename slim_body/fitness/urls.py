from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('training/', Training.as_view(), name='training'),
    path('type-of-training/<str:pk>/', TypeOfTraining.as_view(), name='type-of-training'),
]