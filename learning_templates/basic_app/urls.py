from django.urls import path
from basic_app import views

#Template tagging
urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='others')
    ]