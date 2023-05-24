from django.contrib import admin
from . import models


admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Tag)
admin.site.register(models.Likes_a)
admin.site.register(models.Likes_q)
admin.site.register(models.Profile)
