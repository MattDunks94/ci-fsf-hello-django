from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    # This will be displayed on the page.
    return HttpResponse("Hello!")