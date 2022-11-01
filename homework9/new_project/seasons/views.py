from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>Страница о порах года</h2>')


def winter(request):
    return HttpResponse('<h3>Зима, холодная пора</h3>')


def spring(request):
    return HttpResponse('<h3>Весна, отличная пора</h3>')


def summer(request):
    return HttpResponse('<h3>Лето, теплая пора</h3>')


def autumn(request):
    return HttpResponse('<h3>Осень, унылая пора</h3>')
# Create your views here.
