# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from django.views. import generic View 

def hello(request):
    return HttpResponse("Здравствуй, Мир")