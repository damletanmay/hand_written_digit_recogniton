from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.root),
    path('result', views.hindi_english,name='hindi_english')
]
