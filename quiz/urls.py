from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_random_question, name='get_random_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('results/', views.get_results, name='get_results'),
]
