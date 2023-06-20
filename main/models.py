from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    avatar = models.ImageField(upload_to='main/static/main/avatars', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT) 


class Likes_a(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey(to=Profile, on_delete=models.PROTECT)


class Likes_q(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey(to=Profile, on_delete=models.PROTECT)


class QuestionManager(models.Manager):
    def get_new(self):
        return self.order_by('birth')
    
    def get_hot(self):
        return self.order_by('-likes_q__count')
    
    def get_by_tag(self, tag_search):
        return self.filter(tag__name = tag_search)
    
    def get_popular_tags(self, tags_number):
        all_tags = {}
        for i in self.all():
            for j in i.tag.all():
                if str(j) in all_tags:
                    all_tags[str(j)] = all_tags[str(j)] + 1
                else:
                    all_tags[str(j)] = 1

        popular_tags = sorted(all_tags, key=all_tags.get, reverse=True)
        return popular_tags[:tags_number]
    

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    birth = models.DateTimeField(auto_now=True)
    likes_q = models.ForeignKey(to=Likes_q, on_delete=models.PROTECT)
    tag = models.ManyToManyField(to=Tag)
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    objects = QuestionManager()

    def get_num_answers(self):
        return  Answer.objects.get_answers_by_question_id(self.id).count()
    
    def get_tags(self):
        return self.tag.all()

    def __str__(self):
        return f'Question {self.title[:10]}'


class AnswerManager(models.Manager):
    def get_answers_by_question_id(self, question_id):
        return self.filter(question = question_id)


class Answer(models.Model):
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField()
    likes_a = models.ForeignKey(to=Likes_a, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    objects = AnswerManager()




    
