from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

import random

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(request)
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(
            suggestion=sugg
            )
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list += [temp_sugg]

    context = {
        "title": "CINS465",
        "body":"Hello World",
        "suggestion_list": suggestion_list,
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

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register_view(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")
    else:
        form = forms.RegistrationForm()

    context = {
        "title": "Registration Page",
         "form": form
    }
    return render(request,"registration/register.html", context=context)