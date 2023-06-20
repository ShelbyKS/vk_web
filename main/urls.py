from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot_questions, name='hot_questions'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
    path('tag/<str:tag>/', views.tag_questions, name='tag_questions'),
    path('question/<int:question_id>', views.question, name='question')
]   