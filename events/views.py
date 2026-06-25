from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .models import Event
from .forms import EventForm


def event_list(request):

    events = Event.objects.all()

    return render(
        request,
        'events/event_list.html',
        {'events': events}
    )


def event_add(request):

    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            event = form.save(commit=False)

            event.event_name = event.event_type

            event.save()

            return redirect('event_list')

    else:

        form = EventForm()

    return render(
        request,
        'events/event_form.html',
        {'form': form}
    )


def event_edit(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk
    )

    if request.method == 'POST':

        form = EventForm(
            request.POST,
            instance=event
        )

        if form.is_valid():

            event_obj = form.save(commit=False)

            event_obj.event_name = event_obj.event_type

            event_obj.save()

            return redirect('event_list')

    else:

        form = EventForm(
            instance=event
        )

    return render(
        request,
        'events/event_form.html',
        {'form': form}
    )


def event_delete(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk
    )

    event.delete()

    return redirect('event_list')