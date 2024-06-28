from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from eshop.models import Setting
# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'index.html',context)

def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'about.html', context)

def contactus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'contact.html', context)