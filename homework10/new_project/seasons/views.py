from django.shortcuts import render
from django.http import HttpResponse

dicts = {
    "january": 'Январь-почти весна',
    "february": 'Февраль -только закончилась зима',
    "mart": 'Май - весна',
    "april": 'Апрель - середина весны',
    "may": 'Май - почти лето',
    "june": 'Июнь - тепло',
    "july": 'Июль - можно купаться',
    "august": 'Август - Илья',
    "september": 'Сентябрь - пора в школу',
    "october": 'Октябрь - наступают холода',
    "november": 'Ноябрь - холодно ужас',
    "decemder": 'Декабрь-новый год'
}


def hello(request, hello):
    fun = dicts.get(hello, None)
    if fun:
        return HttpResponse(fun)
    else:
        return HttpResponse("Такого запроса не существует")

def index(request):
    return HttpResponse('Стартовая страница')
