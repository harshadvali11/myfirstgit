from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mounika(request):
    return HttpResponse('<b>This view belongs to Mounika</b>')

def gowthami(request):
    return HttpResponse('<h1>Gowthami is Good Girl</h1>')