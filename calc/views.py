from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("<h3>heello</h3>")


def home(request):
    return render(request, 'home.html')