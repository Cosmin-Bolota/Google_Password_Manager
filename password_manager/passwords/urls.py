from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.createPassword, name="create-password"),
    path('update/<str:pk>/', views.updatePassword, name="update"),
    path('delete/<str:pk>/', views.deletePassword, name="delete"),
]
