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


class CarSearchForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=100, required=False)
    min_year = forms.IntegerField(required=False, label='Min Year')
    max_year = forms.IntegerField(required=False, label='Max Year')
