from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django")

def details(request, question_id):
    return HttpResponse("Question: %s" % question_id)

def results(request, question_id):
    return HttpResponse("Results for: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote for: %s" % question_id)
