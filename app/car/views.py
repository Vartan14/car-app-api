from django.shortcuts import render

from car.models import Car, Owner


def car_table(request):
    cars = Car.objects.all()
    return render(request, 'car_table.html', {'cars': cars})


def owner_detail(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})
