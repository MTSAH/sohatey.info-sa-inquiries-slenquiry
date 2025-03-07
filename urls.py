from django.urls import path
from .views import add_inquiry, get_inquiry,slenquiry

urlpatterns = [
    path('', slenquiry, name='slenquiry'),
    path('add_inquiry/', add_inquiry, name='add_inquiry'),
    path('get_inquiry/', get_inquiry, name='get_inquiry'),
]