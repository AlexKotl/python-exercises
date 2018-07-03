from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'poll/index.html', {
        'latest_questions': latest_questions,
    })

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'poll/details.html', {'question': question})

def results(request, question_id):
    return HttpResponse("Results for: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote for: %s" % question_id)
