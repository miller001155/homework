from django.shortcuts import render
from django.http import HttpResponse
def winter(request):
    return HttpResponse('Зимой холодно но тем не менее')
# Create your views here.
