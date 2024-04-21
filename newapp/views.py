from django.shortcuts import render
from .models import datachange

# Create your views here.
def index(request):
    dest = datachange()
    dest.name = "paris"
    dest.price = 20000
    dest.desc = "paris tower"
    dest.images = "1.png"
    dest.offer = True


    dest1 = datachange()
    dest1.name = "manali"
    dest1.price = 25000
    dest1.desc = "manali hills"
    dest1.images = "2.png"
    dest1.offer = True



    dest2 = datachange()
    dest2.name = "kerala"
    dest2.price = 10000
    dest2.desc = "kerala falls"
    dest2.images = "3.png"
    dest2.offer = False


    dests = [dest, dest1, dest2]

    return render(request, 'index.html', {'est':dests})