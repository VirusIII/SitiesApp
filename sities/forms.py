from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city_name']
        widgets = {'city_name':TextInput(attrs = {'placeholder':'Добавлять здесь...', 'type':'text'})}
