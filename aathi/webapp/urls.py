from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('administration/', views.administration, name='administration'),
    path('contact/', views.contact, name='contact'),
]
