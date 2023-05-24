from main.models import Profile, Question, Answer, Tag, Likes

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.core import management


class Command(BaseCommand):
    help = 'Fill the database'

    @transaction.atomic
    def handle(self, *args, **options):
        models = [Profile, Question, Answer, Tag, Likes]
        for m in models:
            m.objects.all().delete()