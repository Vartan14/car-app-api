from django import forms
from .models import Car, Owner


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = '__all__'
