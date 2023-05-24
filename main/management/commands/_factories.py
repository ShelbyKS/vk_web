import factory
from factory.django import DjangoModelFactory
from main import models
from django.contrib.auth.hashers import make_password
from django.core.files.uploadedfile import SimpleUploadedFile


import random


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User
        strategy = factory.BUILD_STRATEGY

    username = factory.Faker('text', max_nb_chars=30)
    password = make_password('password')


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = models.Profile
        strategy = factory.BUILD_STRATEGY

    avatar = factory.django.ImageField()
    user = factory.SubFactory(UserFactory)


class LikesQFactory(DjangoModelFactory):
    class Meta:
        model = models.Likes_q
        strategy = factory.BUILD_STRATEGY

    user = factory.SubFactory(ProfileFactory)
    count = factory.Faker('pyint', min_value=0, max_value=1000)


class LikesAFactory(DjangoModelFactory):
    class Meta:
        model = models.Likes_a
        strategy = factory.BUILD_STRATEGY

    user = factory.SubFactory(ProfileFactory)
    count = factory.Faker('pyint', min_value=0, max_value=1000)


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = models.Question
        strategy = factory.BUILD_STRATEGY

    title = factory.Faker('text', max_nb_chars=50)
    text = factory.Faker('text', max_nb_chars=300)
    user = factory.SubFactory(ProfileFactory)
    likes_q = factory.SubFactory(LikesQFactory)

    @factory.post_generation
    def tag(self, create, extracted, **kwargs):
        try:
            self.tag.add(*extracted)
        except ValueError:
            print("Can`t fill ManyToMany rel Question-Tag")


class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = models.Answer
        strategy = factory.BUILD_STRATEGY

    text = factory.Faker('text', max_nb_chars=500)
    question = factory.SubFactory(QuestionFactory)
    likes_a = factory.SubFactory(LikesAFactory)
    is_correct = random.choice([True, False])


class TagFactory(DjangoModelFactory):
    class Meta:
        model = models.Tag
        strategy = factory.BUILD_STRATEGY

    name = factory.Faker('word')

