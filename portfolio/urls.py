from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('publications/', views.publications, name='publications'),
    path('contact/', views.contact, name='contact'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
]