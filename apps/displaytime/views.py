from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    context = {
        "date": strftime("%B %d %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    print context
    return render(request, "displaytime/index.html", context)