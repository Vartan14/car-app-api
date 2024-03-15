from django.shortcuts import render, redirect, get_object_or_404

from car.models import Car, Owner
from car.forms import CarForm, OwnerForm


def index(request):
    """
    Redirects to the car table page.

    :param request: HttpRequest object
    :return: Redirect to the car table page
    """
    return redirect('/cars')


def car_table(request):
    """
    View for displaying the car table.

    :param request: HttpRequest object
    :return: Rendered HTML template with the car table
    """
    sort_by = request.GET.get('sort_by', 'id')
    cars = Car.objects.all().order_by(sort_by)
    return render(request, 'car_table.html', {'cars': cars})


def owner_detail(request, owner_id):
    """
    Shows details about a specific owner based on the owner_id.

    :param request: HttpRequest object
    :param owner_id: ID of the owner
    :return: Rendered HTML template with the details of the specified owner
    """
    owner = Owner.objects.get(id=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarForm()

    context = {
        'form': form,
        'title': 'Add car',
    }

    return render(request, 'car_form.html', context)


def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarForm(instance=car)

    context = {
        'form': form,
        'car': car,
        'title': 'Edit car',
    }

    return render(request, 'car_form.html', context)


def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return redirect('cars')


def add_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_car')
    else:
        form = OwnerForm()

    context = {
        'form': form,
        'title': 'Add owner',
    }

    return render(request, 'owner_form.html', context)


def edit_owner(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = OwnerForm(instance=owner)

    context = {
        'form': form,
        'owner': owner,
        'title': 'Edit owner',
    }

    return render(request, 'owner_form.html', context)


def delete_owner(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    owner.delete()
    return redirect('cars')
