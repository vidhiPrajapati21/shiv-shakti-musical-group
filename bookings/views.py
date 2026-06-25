from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import Booking
from .forms import BookingForm
from events.models import Event
from reportlab.lib.utils import ImageReader
from django.conf import settings
import os
from django.shortcuts import redirect
from urllib.parse import quote

def booking_list(request):

    bookings = Booking.objects.all()

    search = request.GET.get('search')
    event_id = request.GET.get('event')

    if search:
        bookings = bookings.filter(
            customer_name__icontains=search
        )

    if event_id:
        bookings = bookings.filter(
            event_id=event_id
        )

    events = Event.objects.all()

    context = {
        'bookings': bookings,
        'events': events,
    }

    return render(
        request,
        'bookings/booking_list.html',
        context
    )


def booking_add(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('booking_list')

    else:

        form = BookingForm()

    return render(
        request,
        'bookings/booking_form.html',
        {'form': form}
    )


def booking_edit(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk
    )

    if request.method == 'POST':

        form = BookingForm(
            request.POST,
            instance=booking
        )

        if form.is_valid():

            form.save()

            return redirect('booking_list')

    else:

        form = BookingForm(
            instance=booking
        )

    return render(
        request,
        'bookings/booking_form.html',
        {'form': form}
    )


def booking_delete(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk
    )

    booking.delete()

    return redirect('booking_list')

def booking_invoice(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="invoice_{booking.id}.pdf"'
    )

    p = canvas.Canvas(response)

    # =========================
    # LOGO
    # =========================

    logo_path = os.path.join(
        settings.BASE_DIR,
        'static',
        'images',
        'logo.jpg'
    )

    print(logo_path)
    print(os.path.exists(logo_path))

    if os.path.exists(logo_path):

        logo = ImageReader(logo_path)

        p.drawImage(
            logo,
            50,
            740,
            width=70,
            height=70
        )

    # =========================
    # COMPANY HEADER
    # =========================

    p.setFont("Helvetica-Bold", 18)

    p.drawString(
        150,
        800,
        "SHIV SHAKTI MUSICAL GROUP"
    )

    p.setFont("Helvetica", 10)

    p.drawString(
        150,
        780,
        "Shiv Shakti Sound, Chetak Marbal ni baju ma, Gandhinagar - Mehsana Link Road, Rampura Chokdi, Mehsana"
    )

    p.drawString(
        150,
        765,
        "Mobile: 9824435234"
    )

    p.line(
        50,
        730,
        550,
        730
    )

    # =========================
    # SOUND TYPE
    # =========================

    if booking.sound_type == "Custom":

        sound_text = (
            f"Custom ({booking.custom_sound_count})"
        )

    else:

        sound_text = booking.sound_type

    # =========================
    # INVOICE DETAILS
    # =========================

    p.setFont("Helvetica", 12)

    p.drawString(
        50,
        690,
        f"Invoice No : INV-{booking.id}"
    )

    p.drawString(
        50,
        660,
        f"Customer Name : {booking.customer_name}"
    )

    p.drawString(
        50,
        630,
        f"Mobile : {booking.mobile}"
    )

    p.drawString(
        50,
        600,
        f"Address : {booking.address}"
    )

    p.drawString(
        50,
        570,
        f"Event Type : {booking.event}"
    )

    p.drawString(
        50,
        540,
        f"Sound Type : {sound_text}"
    )

    p.drawString(
        50,
        510,
        f"Advance Payment : Rs. {booking.advance_payment}"
    )

    p.drawString(
        50,
        480,
        f"Remaining Payment : Rs. {booking.remaining_payment}"
    )

    total = (
        booking.advance_payment +
        booking.remaining_payment
    )

    p.setFont(
        "Helvetica-Bold",
        14
    )

    p.drawString(
        50,
        430,
        f"Total Amount : Rs. {total}"
    )

    p.line(
        50,
        390,
        550,
        390
    )

    p.setFont(
        "Helvetica",
        12
    )

    p.drawString(
        50,
        360,
        "Thank You For Choosing Our Services"
    )

    p.drawString(
        50,
        335,
        "Shiv Shakti Musical Group"
    )

    p.save()

def whatsapp_booking(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk
    )

    message = f"""
Hello {booking.customer_name}

Thank You For Booking With
Shiv Shakti Musical Group

Event : {booking.event}
Sound : {booking.sound_type}

Advance : Rs.{booking.advance_payment}
Remaining : Rs.{booking.remaining_payment}

Thank You
"""

    whatsapp_url = (
        f"https://wa.me/91{booking.mobile}?text="
        f"{quote(message)}"
    )

    return redirect(whatsapp_url)

    return response