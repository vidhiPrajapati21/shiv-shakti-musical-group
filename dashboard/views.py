from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from packages.models import Package
from bookings.models import Booking
from workers.models import Worker
from attendance.models import Attendance
from expenses.models import Expense


@login_required
def dashboard(request):

    total_packages = Package.objects.count()

    total_bookings = Booking.objects.count()

    total_workers = Worker.objects.count()

    total_attendance = Attendance.objects.count()

    # Advance Payment Total
    total_advance = Booking.objects.aggregate(
        Sum('advance_payment')
    )['advance_payment__sum'] or 0

    # Remaining Payment Received
    paid_remaining = Booking.objects.filter(
        payment_status='Paid'
    ).aggregate(
        Sum('remaining_payment')
    )['remaining_payment__sum'] or 0

    # Actual Revenue
    total_revenue = (
        total_advance +
        paid_remaining
    )

    # Pending Payment
    pending_payment = Booking.objects.filter(
        payment_status='Pending'
    ).aggregate(
        Sum('remaining_payment')
    )['remaining_payment__sum'] or 0

    # Total Expenses
    total_expenses = Expense.objects.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    # Net Profit
    net_profit = (
        total_revenue -
        total_expenses
    )

    recent_bookings = Booking.objects.order_by(
        '-id'
    )[:5]

    context = {

        'total_packages': total_packages,
        'total_bookings': total_bookings,
        'total_workers': total_workers,
        'total_attendance': total_attendance,

        'total_revenue': total_revenue,
        'pending_payment': pending_payment,

        'total_expenses': total_expenses,
        'net_profit': net_profit,

        'recent_bookings': recent_bookings,
    }

    return render(
        request,
        'dashboard.html',
        context
    )