from  django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
   path('',views.home, name="home"),
   path('blog/',views.get_all_post,name="blog"),
]
