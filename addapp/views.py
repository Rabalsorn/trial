from django.shortcuts import render
from .models import datachange

# Create your views here.
def reg(request):
    a = datachange.objects.all()
    print(a)
