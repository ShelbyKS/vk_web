from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>about me<h1>")


def hot_questions(request):
    return HttpResponse("<h1>about me!<h1>")


def tag_questions(request):
    return render(request, )


def question(request):
    return render(request, )


def login(request):
    return render(request, )


def signup(request):
    return render(request, )


def ask_question(request):
    return render(request, )