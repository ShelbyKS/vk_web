from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, SettingsForm, AskForm, AnswerForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from .models import Question, Answer, Tag, Likes_a, Likes_q, Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict


def get_user_info(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        return profile


def index(request):
    page = request.GET.get('page')
    posts = pagination(Question.objects.get_new(), page, 10)
    context = {
               'user_info': get_user_info(request),
               'type' : 'new', 
               'popular_tags' : Question.objects.get_popular_tags(10),
               'page': page,
               'posts': posts
              }
    return render(request, 'main/index/index.html', context)



def hot_questions(request):
    page = request.GET.get('page')
    posts = pagination(Question.objects.get_hot(), page, 3)

    context = {
               'user_info': get_user_info(request),
               'type' : 'hot', 
               'user_status' : 'unlogin',
               'popular_tags' : Question.objects.get_popular_tags(10),
               'page': page,
               'posts': posts
              }

    return render(request, 'main/index/index.html', context)


def tag_questions(request, tag):
    if tag in list(Tag.objects.values_list('name', flat=True)):
        page = request.GET.get('page')
        posts = pagination(Question.objects.get_by_tag(tag), page, 2)
        context = {
               'user_info': get_user_info(request),
               'type' : 'tag', 
               'popular_tags' : Question.objects.get_popular_tags(10),
               'page': page,
               'posts': posts,
               'tag': tag
              }
        return render(request, 'main/index/index.html', context)
    
    else:
        return HttpResponseNotFound()


@csrf_exempt
def login(request):
    context = {'popular_tags' : Question.objects.get_popular_tags(10)}
    
    if request.method == "GET":
        login_form = LoginForm()

    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request=request, **login_form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else: 
                login_form.add_error(None, "Wrong username or password")

    context['form'] = login_form
    return render(request, 'main/user/login.html', context)
          

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


def signup(request):
    context = {'popular_tags' : Question.objects.get_popular_tags(10)}
    
    if request.method == "GET":
        registration_form = RegistrationForm()

    elif request.method == "POST":
        registration_form = RegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():
            user = registration_form.save()
            if user:
                return redirect(reverse('index'))
            else: 
                registration_form.add_error(None, "Registration error")

    context['form'] = registration_form
    return render(request, 'main/user/registration.html', context)


@login_required
def ask(request):
    context = {
        'user_info': get_user_info(request),
        'popular_tags' : Question.objects.get_popular_tags(10)
    }

    if request.method == "GET":
        ask_form = AskForm()
    elif request.method == "POST":
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            #ask_form.save()
            return redirect(reverse('index'))

    context['form'] = ask_form
    return render(request, 'main/ask/ask.html', context)


@login_required
def settings(request):
    context = {
            'popular_tags' : Question.objects.get_popular_tags(10),
            'user_info': get_user_info(request)
    }
    
    if request.method == "GET":
        current_settings = model_to_dict(request.user)
        settings_form = SettingsForm(initial=current_settings)

    elif request.method == "POST":
        settings_form = SettingsForm(request.POST, request.FILES)
        if settings_form.is_valid():
            #settings_form.save()
            return redirect(reverse('index'))

    context['form'] = settings_form
    return render(request, 'main/user/settings.html', context)


def question_page(request, question_id):
    question = Question.objects.get(id = question_id)
    if question in Question.objects.all():
        page = request.GET.get('page')
        answers = pagination(Answer.objects.get_answers_by_question_id(question_id), page, 2)
    else:
        return HttpResponse("No such question")
    
    context = {
                'question' : question,
                'user_info': get_user_info(request),
                'page': page,
                'posts': answers,
                'popular_tags' : Question.objects.get_popular_tags(10)
            } 
    if request.method == "GET":
         answer_form = AnswerForm()

    elif request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            #answer_form.save()
            return redirect(reverse('index'))
        
    context['form'] = answer_form
    return render(request, 'main/question_page/index.html', context)




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

