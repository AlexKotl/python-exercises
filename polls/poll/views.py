from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'poll/index.html', {
        'latest_questions': latest_questions,
    })    

def details(request, question_id):
    return HttpResponse("Question: %s" % question_id)

def results(request, question_id):
    return HttpResponse("Results for: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote for: %s" % question_id)
