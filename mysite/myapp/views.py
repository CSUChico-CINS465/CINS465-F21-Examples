from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    some_list = models.SuggestionModel.objects.all()
    context = {
        "title": "CINS465",
        "body":"Hello World",
        "some_list": some_list,
        "form": form
    }
    return render(request,"index.html", context=context)

def delete_random(request):
    some_list = models.SuggestionModel.objects.all()
    some_int = random.randrange(len(some_list))
    some_instance = some_list[some_int]
    some_instance.delete()
    print(some_int)
    return redirect("/")