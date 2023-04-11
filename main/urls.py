from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
    path('hot/', views.hot_questions),
    path('tag/tag1/', views.tag_questions),
    path('question/q_number/', views.question),
    path('login/', views.login),
    path('signup/', views.signup),
    path('ask/', views.ask_question),
]