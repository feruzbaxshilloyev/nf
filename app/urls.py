from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact1, name='contact'),
    path('ct_d/<int:pk>', category, name='ct_d'),
    path('n_d/<int:pk>/', news_detail, name='n_d'),
    path('comment/<int:pk>/', comment, name='comment'),
    path('l_d/<int:pk>/', rate_like, name='l_d'),
    path('d_d/<int:pk>/', rate_dis, name='d_d'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile_edit/', profile_edit, name='edit'),
    path('com_edit/<int:pk>/', edit_comment, name='c_edit'),
    path('c_delete/<int:pk>/', delete_comment, name='c_del'),
    path('user_com/', user_com, name='user_com'),
    path('add_new/', add_new, name='add_new'),
    path('add_ctg/', add_ctg, name='add_ctg'),
    path('add_admin/', add_admin, name='add_admin'),
]
