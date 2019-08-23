
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):

    if(request.method == "POST"):
        req = request.POST
        if 'add' in req:
            form = CityForm(req)
            form.save()
        elif 'delete' in req:

            City.objects.filter(id=req.copy().pop('delete')[0]).delete()
        elif 'list' in req:
            print(req)


    # if(request.method == "POST"):
    #     form = CityForm(request.POST)
    #     form.save()
    #req["delete"]
    form = CityForm()

    сities = City.objects.all()
    all_сities =[]
    for city in сities:
        city_info = {
        "city_name":city.city_name,
        "city_id":city.id,
        }
        all_сities.append(city_info)

    context = {'all_info':all_сities, "form":form}
    return render(request, 'sities/index.html',context)

def add(request):
    return render(request,'sities/index.html')

def list(request):
    return render(request,'sities/index.html')

def delete(request):
    return render(request,'sities/index.html')
# Create your views here.
