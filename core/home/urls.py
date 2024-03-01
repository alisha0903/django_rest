from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('student/',post_Student,name="Post_student"),
    path('update-student/<id>', update_Student,name="update-student")
]
