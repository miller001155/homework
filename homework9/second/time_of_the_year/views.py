from django.shortcuts import render
from django.http import HttpResponse


def time_of_the_year(request):
    return HttpResponse('Бывает 4 поры года (Зима, Весна, Лето и Осень)')
# Create your views here.
