from django.conf.urls import include, url
from django.urls import path
from app import views

urlpatterns = [
    url(r'^', views.hello, name = 'hello'),
    url(r'^homes/', views.home, name = 'home'),
    
]
