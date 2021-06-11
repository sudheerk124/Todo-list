from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details,name='details'),
    path('details/<id>', views.details,name='details'),
    path('add/', views.add, name='add')
]
