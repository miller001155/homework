from django.shortcuts import render
from django.http import HttpResponse


def summer(request):
    return HttpResponse('Летом тепло и хорошо ')
# Create your views here.
