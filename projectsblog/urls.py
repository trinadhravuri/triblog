from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('allprojects',views.allprojects, name='allprojects'),
    path('addproject',views.addproject,name='addproject'),
]
