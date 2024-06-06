from django.shortcuts import render, redirect, get_object_or_404

from car.models import Car, Owner
from car.forms import CarForm, OwnerForm, CarSearchForm
from django.utils import timezone
from django.db.models import Count


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
    """
    if request.method == 'GET':
        form = CarSearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data.get('keyword')
            min_year = form.cleaned_data.get('min_year')
            max_year = form.cleaned_data.get('max_year')
            sort_by = request.GET.get('sort_by', 'id')

            cars = Car.objects.all().order_by(sort_by)

            if keyword:
                cars = cars.filter(brand__icontains=keyword)
            if min_year:
                cars = cars.filter(year__gte=min_year)
            if max_year:
                cars = cars.filter(year__lte=max_year)

    else:
        form = CarSearchForm()
        cars = Car.objects.all()

    return render(request, 'car_table.html', {'cars': cars, 'form': form})


def owner_detail(request, owner_id):
    """
    Shows details about a specific owner based on the owner_id.
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


def statistics(request):
    # Total records in Owner table
    owner_count = Owner.objects.count()

    # Total records in Car table
    car_count = Car.objects.count()

    # Total records in Owner table for the last month
    last_month = timezone.now() - timezone.timedelta(days=30)
    owner_count_last_month = Owner.objects.filter(date_created__gte=last_month).count()

    # Total records in Owner table for the last month
    car_count_last_month = Car.objects.filter(date_created__gte=last_month).count()

    # The last record in Owner table
    last_owner_record = Owner.objects.latest('date_created')

    # The record in Owner table with the largest number of related records in Car table
    owner_with_most_cars = Owner.objects.annotate(num_cars=Count('car')).order_by('-num_cars').first()

    context = {
        'owner_count': owner_count,
        'car_count': car_count,
        'owner_count_last_month': owner_count_last_month,
        'car_count_last_month': car_count_last_month,
        'last_owner_record': last_owner_record,
        'owner_with_most_cars': owner_with_most_cars,
    }

    return render(request, 'statistics.html', context)