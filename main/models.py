from django.db import models

NEW_QUESTIONS = [
    {
        'id': (i+1),
        'title': f'Question {i+1}',
        'text': f'Text {i+1}',
        'answers': i,
        'tags': ['Python', 'CSS', 'Django'],
        'rating': '3',
        'avatar': 'main/img/avatar-1.jpg'
    } for i in range(10)
]

HOT_QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i+1}',
        'text': f'Text {i+1}',
        'answers': i,
        'tags': ['Python', 'CSS', 'Django'],
        'rating': 5,
        'avatar': 'main/img/avatar-1.jpg'
    } for i in range(9, -1, -1)
]

USER_INFO = {
        'nickname' : 'Alexandr',
        'photo' : 'main/img/avatar-2.jpg',
        'login' : 'shelby',
        'email': 'krylov.sanches@mail.ru'
}

PYTHON_QUESTIONS = [
    {
        'id': i,
        'title': f'Python question {i+1}',
        'text': f'Text {i+1}',
        'answers': i,
        'tags': ['Python', 'CSS', 'Django'],
        'rating': '3',
        'avatar': 'main/img/avatar-1.jpg'
    } for i in range(4)
]

POPULAR_TAGS = ['Python', 'Django']

