from django.urls import path
from .views import *

from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        booking_list,
        name='booking_list'
    ),

    path(
        'add/',
        booking_add,
        name='booking_add'
    ),

    path(
        'edit/<int:pk>/',
        booking_edit,
        name='booking_edit'
    ),

    path(
        'delete/<int:pk>/',
        booking_delete,
        name='booking_delete'
    ),

    path(
        'invoice/<int:pk>/',
        booking_invoice,
        name='booking_invoice'
    ),

    path(
    'whatsapp/<int:pk>/',
    whatsapp_booking,
    name='whatsapp_booking'
),

]