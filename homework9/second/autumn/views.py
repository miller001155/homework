from django.shortcuts import render
from django.http import HttpResponse


def autumn(request):
    return HttpResponse('Осень холодная пора ')
# Create your views here.
