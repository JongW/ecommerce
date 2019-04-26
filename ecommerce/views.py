from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {"title": "home page"}
    return render(request, "home_page.html", context)


def about_page(request):
    context = {"title": "about page"}
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {"title": "contact page"}
    if request.method == "POST":
        print(request.POST.get("fullname"))
    return render(request, "form.html", context)


def home_page_old(request):
    # When you go to a url this function is called
    # Takes request as an argument and returns the Http Response
    return HttpResponse("<h1>Hello World<h1>")
