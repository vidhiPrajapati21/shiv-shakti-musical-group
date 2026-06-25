from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .models import Attendance
from .forms import AttendanceForm
from django.db.models import Sum
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def attendance_list(request):

    attendances = Attendance.objects.all()

    return render(
        request,
        'attendance/attendance_list.html',
        {'attendances': attendances}
    )


def attendance_add(request):

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('attendance_list')

    else:

        form = AttendanceForm()

    return render(
        request,
        'attendance/attendance_form.html',
        {'form': form}
    )


def attendance_edit(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            form.save()

            return redirect('attendance_list')

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        'attendance/attendance_form.html',
        {'form': form}
    )


def attendance_delete(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    attendance.delete()

    return redirect('attendance_list')

from django.db.models import Sum

def salary_report(request):

    workers_salary = {}

    attendances = Attendance.objects.all()

    for att in attendances:

        if att.worker.name not in workers_salary:

            workers_salary[att.worker.name] = 0

        workers_salary[att.worker.name] += att.salary

    return render(
        request,
        'attendance/salary_report.html',
        {'workers_salary': workers_salary}
    )

def monthly_salary_report(request):

    month = request.GET.get('month')

    attendances = Attendance.objects.all()

    if month:

        attendances = attendances.filter(
            date__month=month
        )

    workers_salary = {}

    for att in attendances:

        worker_name = att.worker.name

        if worker_name not in workers_salary:

            workers_salary[worker_name] = 0

        workers_salary[worker_name] += att.salary

    context = {
        'workers_salary': workers_salary
    }

    return render(
        request,
        'attendance/monthly_salary_report.html',
        context
    )

def salary_report_pdf(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="salary_report.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)

    p.drawString(
        200,
        800,
        "Monthly Salary Report"
    )

    y = 750

    p.setFont("Helvetica", 12)

    p.drawString(50, y, "Worker")
    p.drawString(300, y, "Total Salary")

    y -= 30

    workers_salary = {}

    attendances = Attendance.objects.all()

    for att in attendances:

        worker_name = att.worker.name

        if worker_name not in workers_salary:

            workers_salary[worker_name] = 0

        workers_salary[worker_name] += att.salary

    for worker, salary in workers_salary.items():

        p.drawString(
            50,
            y,
            worker
        )

        p.drawString(
            300,
            y,
            f"Rs. {salary}"
        )

        y -= 25

    p.save()

    return response