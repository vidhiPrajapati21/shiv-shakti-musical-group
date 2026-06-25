from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        event_list,
        name='event_list'
    ),

    path(
        'add/',
        event_add,
        name='event_add'
    ),

    path(
        'edit/<int:pk>/',
        event_edit,
        name='event_edit'
    ),

    path(
        'delete/<int:pk>/',
        event_delete,
        name='event_delete'
    ),

]