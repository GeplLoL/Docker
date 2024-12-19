
from django.urls import path
from . import views

urlpatterns = [
    path('', views.toy_list, name='toy_list'),
    path('toy/<int:pk>/', views.toy_detail, name='toy_detail'),
    path('toy/new/', views.toy_create, name='toy_create'),
    path('toy/<int:pk>/edit/', views.toy_edit, name='toy_edit'),
    path('toy/<int:pk>/delete/', views.toy_delete, name='toy_delete'),
]



