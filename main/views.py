from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    page = request.GET.get('page')
    posts = pagination(models.NEW_QUESTIONS, page, 3)
    context = {
               'user_info': models.USER_INFO,
               'type': 'new', 
               'user_status':'unlogin',
               'popular_tags' : models.POPULAR_TAGS,
               'page': page,
               'posts': posts
              }
    
    return render(request, 'main/index/index.html', context)


def hot_questions(request):
    page = request.GET.get('page')
    posts = pagination(models.NEW_QUESTIONS, page, 4)
    context = {
               'user_info': models.USER_INFO,
               'type': 'hot', 
               'user_status':'login',
               'popular_tags' : models.POPULAR_TAGS,
               'page': page,
               'posts': posts
              }
    
    return render(request, 'main/index/index.html', context)


def tag_questions(request, tag):
    if tag in models.TAG_QUESTIONS:
        page = request.GET.get('page')
        print(tag)
        posts = pagination(models.TAG_QUESTIONS[tag], page, 2)
        context = {
                'user_info': models.USER_INFO,
                'type': 'tag', 
                'user_status':'login',
                'popular_tags' : models.POPULAR_TAGS,
                'tag': tag,
                'page': page,
                'posts': posts
                }
        
        return render(request, 'main/index/index.html', context)
    
    else:
        return HttpResponse("No such tag")


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
    if (int(question_id) < len(models.NEW_QUESTIONS)):
        page = request.GET.get('page')
        answers = pagination(models.ANSWERS, page, 2)

        context = {
            'question' : models.NEW_QUESTIONS[question_id - 1],
            'user_status':'login',
            'user_info': models.USER_INFO,
            'answers': models.ANSWERS,
            'page': page,
            'posts': answers              
        } 
        return render(request, 'main/question_page/index.html', context)

    else:
        return HttpResponse("No such question")


def pagination(objects, page, per_page = 10):
    object_list = objects
    paginator = Paginator(object_list, per_page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts
