from django.urls import path
from .views import index, hello

urlpatterns = [
    path('<hello>', hello),
    path('', index),
]
