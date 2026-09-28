from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Backend!")


def about(request):
    return HttpResponse("This is the About endpoint.")


def users(request):
    data = {
        "users": ["Gitesh", "Harshit", "Mohit"]
    }
    return JsonResponse(data)


def products(request):
    data = {
        "products": ["Tofee", "Bread", "Cake"]
    }
    return JsonResponse(data)


def contact(request):
    return HttpResponse("Contact us at giteshsharma2409@gmail.com")


def go_to_about(request):
    return redirect("about")


def webpage(request):
    return render(request, "index.html")