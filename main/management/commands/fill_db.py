from main.models import Profile, Question, Answer, Tag, Likes_a, Likes_q
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from main.management.commands._factories import (
    TagFactory,
    QuestionFactory,
    ProfileFactory,
    AnswerFactory,
    LikesAFactory,
    LikesQFactory,
    UserFactory
)

import random


class Command(BaseCommand):
    help = 'Fill the database'

    def add_arguments(self, parser):
        parser.add_argument('ratio', nargs='?', type=int, default=10000)

    @transaction.atomic
    def handle(self, *args, **options):
        models = [Profile, Question, Answer, Tag, Likes_a, Likes_q]
        #for m in models:
            #m.objects.all().delete()

        ratio = options['ratio']

        users = User.objects.bulk_create(UserFactory() for _ in range(ratio))
        profiles = []
        for i in range(ratio):
            profile = ProfileFactory.create(avatar = '/main/img/avatar-3.jpg' ,user = users[i])
            profiles.append(profile)
        
        tag = Tag.objects.bulk_create(TagFactory() for _ in range(ratio))

        likes_a = []
        for _ in range(ratio * 100):
            like_a = LikesAFactory.create(user = random.choice(profiles))
            likes_a.append(like_a)

        likes_q = []
        for _ in range(ratio * 100):
            like_q = LikesQFactory.create(user = random.choice(profiles))
            likes_q.append(like_q)

        questions = []
        for _ in range(ratio * 10):
            question = QuestionFactory.create( user=random.choice(profiles),
                                                tag=random.choices(tag, k=random.choice([1, 2, 3])),
                                                likes_q = random.choice(likes_q)
                                                )
            questions.append(question)

        answers = [] 
        for _ in range(ratio * 100):
            answer = AnswerFactory.create(
                question = random.choice(questions),
                likes_a = random.choice(likes_a)
            )
            answers.append(answer)
