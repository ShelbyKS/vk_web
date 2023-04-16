from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    context = {'questions': models.NEW_QUESTIONS, 
               'user_info': models.USER_INFO,
               'type': 'new', 
               'user_status':'unlogin',
               'popular_tags' : models.POPULAR_TAGS
              }
    return render(request, 'main/index/index.html', context)


def hot_questions(request):
    context = {'questions': models.HOT_QUESTIONS, 
               'user_info': models.USER_INFO,
               'type': 'hot', 
               'user_status':'login',
               'popular_tags' : models.POPULAR_TAGS
              }
    return render(request, 'main/index/index.html', context)


def tag_questions(request):
    context = {
        'questions': models.PYTHON_QUESTIONS,
        'user_info': models.USER_INFO, 
        'type': 'tag',
        'user_status':'login',
        'popular_tags' : models.POPULAR_TAGS,
        'tag': 'Python'
    }
    return render(request, 'main/index/index.html', context)


def login(request):
    message = 'Wrong login or password'
    context = {
        'user_info': models.USER_INFO,
        'user_status':'unlogin',
        'message' : message,
        'popular_tags' : models.POPULAR_TAGS
    }
    return render(request, 'main/user/login.html', context)


def signup(request):
    message = 'password are different'
    context = {
        'user_info': models.USER_INFO,
        'user_status':'unlogin',
        'message' : message,
        'popular_tags' : models.POPULAR_TAGS
    }
    return render(request, 'main/user/registration.html', context)


def ask(request):
    message = 'fill all fields'
    context = {
        'user_info': models.USER_INFO,
        'user_status':'login',
        'message' : message,
        'popular_tags' : models.POPULAR_TAGS
    }
    return render(request, 'main/ask/ask.html', context)


def settings(request):
    message = 'fill all fields'
    context = {
        'user_info': models.USER_INFO,
        'user_status':'login',
        'message' : message,
        'popular_tags' : models.POPULAR_TAGS
    }
    return render(request, 'main/user/settings.html', context)


def question_page(request, question_id):
    context = {'question' : models.NEW_QUESTIONS[question_id]} #сделать проверку на выход из диапазона
    return render(request, 'main/question/question_page.html', context)




