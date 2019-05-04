from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    context = {"title": "home page"}
    return render(request, "home_page.html", context)


def about_page(request):
    context = {"title": "about page"}
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {"title": "contact page", "contact_form": contact_form}

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))

    return render(request, "form.html", context)


def home_page_old(request):
    # When you go to a url this function is called
    # Takes request as an argument and returns the Http Response
    return HttpResponse("<h1>Hello World<h1>")
