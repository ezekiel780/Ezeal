from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Numerical, name='Numerical'),
]
