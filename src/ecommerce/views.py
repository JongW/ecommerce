from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {"title": "home page",
               "premium_content" : "yea, this is it. This is the premium content"}
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


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {"login_form": login_form}

    if login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context["login_form"] = LoginForm()
            print("Logged in!")
            return redirect("/login")
        else:
            print("Not valid user")

    return render(request, "auth/login_page.html", context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
   
    context = {
        "register_form": register_form
    }

    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register_page.html", context)
