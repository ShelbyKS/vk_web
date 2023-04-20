from django.db import models

text_question = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestias repellat consequatur incidunt quia animi autem aut sunt exercitationem. Repellat veniam excepturi itaque. Possimus, mollitia dolores at facilis ad vel. Unde voluptatum nam nemo, dolores sed cum eaque eveniet eius accusantium commodi! Animi nostrum dolore aut. Beatae itaque minus architecto similique dolore modi quam dolores aperiam exercitationem consequatur quibusdam consectetur eaque, maxime quis sint, veritatis quas autem officiis temporibus doloribus accusantium tempore saepe amet. Fugiat quo veniam pariatur aliquam cum exercitationem explicabo ratione ut recusandae laudantium alias quo'

text_answer = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestias repellat consequatur incidunt quia animi autem aut sunt exercitationem. Repellat veniam excepturi itaque. Possimus, mollitia dolores at facilis ad vel. Unde voluptatum nam nemo, dolores sed cum eaque eveniet eius accusantium'

NEW_QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'text': text_question,
        'answers': i, 
        'tags': ['Python', 'CSS', 'Django'],
        'rating': 3,
        'avatar': 'main/img/avatar-1.jpg'
    } for i in range(1, 13, 1)
]


TAG_QUESTIONS = {
        'Python' : [
                    {
                        'id': i,
                        'title': f'Python question {i}',
                        'text': text_question,
                        'answers': i, 
                        'tags': ['Python', 'CSS', 'Django'],
                        'rating': 3,
                        'avatar': 'main/img/avatar-1.jpg'
                    } for i in range(1, 13, 1)],
        'Django' : [
                    {
                        'id': i,
                        'title': f'Django question {i}',
                        'text': text_question,
                        'answers': i, 
                        'tags': ['Python', 'CSS', 'Django'],
                        'rating': 3,
                        'avatar': 'main/img/avatar-1.jpg'
                    } for i in range(1, 5, 1)]

}


ANSWERS = [
    {
        'id': i,
        'user_avatar': 'main/img/avatar-3.jpg',
        'rating': 4,
        'text': text_answer,
        'correct': 'yes'
    } for i in range(1, 3)
]

USER_INFO = {
        'nickname' : 'Alexandr',
        'photo' : 'main/img/avatar-2.jpg',
        'login' : 'shelby',
        'email': 'krylov.sanches@mail.ru'
}

POPULAR_TAGS = ['Python', 'Django']

