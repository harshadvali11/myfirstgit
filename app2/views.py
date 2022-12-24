from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prakash(request):
    return HttpResponse('<i>Prakash friend is Very Bad Boy</i>')

def revi(request):
    return HttpResponse('<marquee><h2>Its Revi Da, Thambi Madiri</h2></marquee>')