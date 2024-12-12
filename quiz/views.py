from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .models import Question, QuizSession
from django.contrib.auth.decorators import login_required
import random

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('start_quiz')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

# Logout view (Django provides this built-in)
# Django's logout view doesn't require any changes in views.py

@login_required
def start_quiz(request):
    session, created = QuizSession.objects.get_or_create(user=request.user)
    session.total_questions = 0
    session.correct_answers = 0
    session.incorrect_answers = 0
    session.asked_questions = []
    session.save()
    return redirect('get_random_question')

@login_required
def get_random_question(request):
    session = QuizSession.objects.get(user=request.user)

    if session.total_questions >= 10:
        return redirect('get_results')

    remaining_questions = Question.objects.exclude(id__in=session.asked_questions)
    if not remaining_questions.exists():
        return render(request, 'questions.html', {'error': 'No more questions available.'})

    question = random.choice(remaining_questions)
    session.asked_questions.append(question.id)
    session.save()

    return render(request, 'questions.html', {
        'question': question,
        'question_number': session.total_questions + 1
    })

@login_required
def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('selected_option')
        question = Question.objects.get(id=question_id)
        session = QuizSession.objects.get(user=request.user)

        session.total_questions += 1
        if selected_option == question.correct_option:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1

        session.save()
        return redirect('get_random_question')

@login_required
def get_results(request):
    session = QuizSession.objects.get(user=request.user)
    return render(request, 'result.html', {
        'total_questions': session.total_questions,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers
    })
