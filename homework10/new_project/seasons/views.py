from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

dicts = {  # создаем словарь для месяцев
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


def hello(request, hello):  # создаем функцию, которая принимает значение hello
    fun = dicts.get(hello, None)  # обращаемся к словарю и берем значение по ключу
    if fun:  # если такой ключ в словаре
        return HttpResponse(fun)  # то выводим его значение на экран
    else:
        return HttpResponseNotFound("Такого запроса не существует")  # если такого значения нет

def index(request):
    return HttpResponse('Стартовая страница')
