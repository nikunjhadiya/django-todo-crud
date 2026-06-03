from django.urls import path
from .views import *

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
    path('crestore/<int:pk>/', crestore, name='crestore'),
    path('cdelete/<int:pk>/', cdelete, name='cdelete'),
    path('trestoreall/', trestoreall, name='trestoreall'),
    path('tdeleteall/', tdeleteall, name='tdeleteall'),
    path('trestore/<int:pk>/', trestore, name='trestore'),
    path('tdelete/<int:pk>/', tdelete, name='tdelete'),
    path('trashrestoreall/', trashrestoreall, name='trashrestoreall'),
    path('trashdeleteall/', trashdeleteall, name='trashdeleteall'),

]