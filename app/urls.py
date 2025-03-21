from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact1, name='contact'),
    path('ct_d/<int:pk>', category, name='ct_d'),
    path('n_d/<int:pk>/', news_detail, name='n_d')
]
