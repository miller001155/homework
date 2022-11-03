from django.shortcuts import render
from django.http import HttpResponse

dicts = {
    "decemder": 'новый год',
    "january": 'почти весна',
    "february": 'только закончилась зива',
    "mart": 'весна',
    "april": 'заканчивается весна',
    "may": 'почти лето',
    "june": 'тепло',
    "july": 'можно купаться',
    "august": 'Илья',
    "september": 'пора в школу',
    "october": 'наступают холода',
    "november": 'холодно ужу',
}
def index(request, index):
    if index == dicts.get('index', None):
        return HttpResponse('index')
    else:
        return HttpResponse("Такого запроса не существует")
