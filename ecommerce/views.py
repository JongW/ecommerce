from django.http import HttpResponse

from django.shortcuts import render


def home_page(request):
    # When you go to a url this function is called
    # Takes request as an argument and returns the Http Response
    return HttpResponse("Hello World")
