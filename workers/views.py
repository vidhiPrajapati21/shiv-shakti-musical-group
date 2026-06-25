from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .models import Worker
from .forms import WorkerForm


def worker_list(request):

    workers = Worker.objects.all()

    return render(
        request,
        'workers/worker_list.html',
        {'workers': workers}
    )


def worker_add(request):

    if request.method == 'POST':

        form = WorkerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('worker_list')

    else:

        form = WorkerForm()

    return render(
        request,
        'workers/worker_form.html',
        {'form': form}
    )


def worker_edit(request, pk):

    worker = get_object_or_404(
        Worker,
        pk=pk
    )

    if request.method == 'POST':

        form = WorkerForm(
            request.POST,
            instance=worker
        )

        if form.is_valid():

            form.save()

            return redirect('worker_list')

    else:

        form = WorkerForm(
            instance=worker
        )

    return render(
        request,
        'workers/worker_form.html',
        {'form': form}
    )


def worker_delete(request, pk):

    worker = get_object_or_404(
        Worker,
        pk=pk
    )

    worker.delete()

    return redirect('worker_list')