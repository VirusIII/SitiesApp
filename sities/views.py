import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
import json
from django.http import HttpResponse

def index(request):
    respond = {'all_сities':[]}
    if(request.method == 'POST'):
        req = request.POST
        if 'add' in req:
            requests.get('http://localhost:3000/sities/add/?cityname={}'.format(req.__getitem__('city_name')))
        elif 'delete' in req:
            requests.get('http://localhost:3000/sities/delete/?id={}'.format(req.copy().pop('delete')[0]))
        elif 'list' in req:
            respond = requests.get('http://localhost:3000/sities/list/').json()

    form = CityForm()
    context = {'all_info':respond['all_сities'], 'form':form}
    return render(request, 'sities/index.html',context)

def add(request):
    form = City(city_name = request.GET.get('cityname', 'Варшава'))
    form.save()
    return render(request,'sities/index.html')

def list(request):
    all_сities =[]
    сities = City.objects.all()
    for city in сities:
        city_info = {
        'city_name':city.city_name,
        'city_id':city.id,
        }
        all_сities.append(city_info)
        response = {'all_сities':all_сities}
    return HttpResponse(json.dumps(response),content_type='application/json')

def delete(request):
    City.objects.filter(id=request.GET.get('id', 0)).delete()
    return render(request,'sities/index.html')
# Create your views here
