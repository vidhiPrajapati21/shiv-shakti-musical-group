from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        worker_list,
        name='worker_list'
    ),

    path(
        'add/',
        worker_add,
        name='worker_add'
    ),

    path(
        'edit/<int:pk>/',
        worker_edit,
        name='worker_edit'
    ),

    path(
        'delete/<int:pk>/',
        worker_delete,
        name='worker_delete'
    ),
]