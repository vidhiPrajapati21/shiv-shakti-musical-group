from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Package
from .forms import PackageForm


@login_required
def package_list(request):

    packages = Package.objects.all()

    return render(
        request,
        'packages/package_list.html',
        {'packages': packages}
    )


@user_passes_test(lambda u: u.is_superuser)
def package_add(request):

    if request.method == 'POST':

        form = PackageForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('package_list')

    else:

        form = PackageForm()

    return render(
        request,
        'packages/package_form.html',
        {'form': form}
    )


@user_passes_test(lambda u: u.is_superuser)
def package_edit(request, pk):

    package = get_object_or_404(
        Package,
        pk=pk
    )

    if request.method == 'POST':

        form = PackageForm(
            request.POST,
            instance=package
        )

        if form.is_valid():

            form.save()

            return redirect('package_list')

    else:

        form = PackageForm(
            instance=package
        )

    return render(
        request,
        'packages/package_form.html',
        {'form': form}
    )


@user_passes_test(lambda u: u.is_superuser)
def package_delete(request, pk):

    package = get_object_or_404(
        Package,
        pk=pk
    )

    package.delete()

    return redirect('package_list')