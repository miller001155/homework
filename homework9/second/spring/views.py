from django.shortcuts import render
from django.http import HttpResponse


def spring(request):
    return HttpResponse('Весна веселая пора')
# Create your views here.
