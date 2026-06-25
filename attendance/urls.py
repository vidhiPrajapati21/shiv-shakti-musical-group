from django.urls import path
from .views import *

urlpatterns = [

    path('', attendance_list, name='attendance_list'),

    path('add/', attendance_add, name='attendance_add'),

    path('edit/<int:pk>/', attendance_edit, name='attendance_edit'),

    path('delete/<int:pk>/', attendance_delete, name='attendance_delete'),

    path(
    'salary-report/',
    salary_report,
    name='salary_report'
),

    path(
    'monthly-salary-report/',
    monthly_salary_report,
    name='monthly_salary_report'
),

    path(
    'salary-report-pdf/',
    salary_report_pdf,
    name='salary_report_pdf'
),

]