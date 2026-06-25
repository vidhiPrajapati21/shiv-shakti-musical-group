from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        package_list,
        name='package_list'
    ),

    path(
        'add/',
        package_add,
        name='package_add'
    ),

    path(
        'edit/<int:pk>/',
        package_edit,
        name='package_edit'
    ),

    path(
        'delete/<int:pk>/',
        package_delete,
        name='package_delete'
    ),

]