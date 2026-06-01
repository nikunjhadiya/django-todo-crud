from django.urls import path
from .views import *
from base import views

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('completed/', completed, name='completed'),
    path('trash/', trash, name='trash'),
    path('about/', about, name='about'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('complete/<int:pk>/', complete, name='complete'),
    path('completeall/', completeall, name='completeall'),
    path('deleteall/', deleteall, name='deleteall'),

]