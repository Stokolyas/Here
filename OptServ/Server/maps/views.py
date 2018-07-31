from django.shortcuts import render
from django.http import HttpResponse
from .models import Bunker
import json

def fill(request):
    if request.method == "POST":
        ID = request.POST.get("id")
        print(ID)
        bunker = Bunker.objects.get(id = ID)
        bunker.Full = 1
        bunker.save()
        return render('maps/sss.html',
            {'bunkers': bunkers, 'Full': Full})
    else:
        return HttpResponse('Please submit a search term.')

def  index ( request ):
    bunkers = Bunker.objects.order_by('Full')
    context = {'bunkers': bunkers}
    return render(request, 'maps/home.html', context)


def  route ( request ):
    bunkers = Bunker.objects.filter(remove = True)
    context = {'bunkers': bunkers}
    return render(request, 'maps/route.html', context)


def  ind ( request ):
    bunkers = Bunker.objects.filter(remove = True)
    context = {'bunkers': bunkers}
    return render(request, 'maps/sss.html', context)

#  функция принимающя значение заполненности конкретного контейнера и
# сохраняющая это значение
