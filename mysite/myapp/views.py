from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

from . import models

# Create your views here.
def index(request):
    some_list = models.SuggestionModel.objects.all()
    context = {
        "title": "CINS465",
        "body":"Hello World",
        "some_list": some_list,
    }
    return render(request,"index.html", context=context)

def dumb(request):
    some_list = models.SuggestionModel.objects.all()
    some_int = random.randrange(len(some_list))
    some_instance = some_list[some_int]
    some_instance.delete()
    print(some_int)
    return redirect("/")