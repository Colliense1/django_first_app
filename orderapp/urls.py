from django.urls import path
from . import views

urlpatterns = [
    path('order/allorders/', views.order),
    path('', views.global_home),
]