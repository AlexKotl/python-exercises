from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from .models import Question

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        ''' Return last five questions '''
        return Question.objects.order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'poll/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/details.html', {
            question: question,
            error_message: "Choice not existed",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

# OLD STYLE VIEWS, NOT USED
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'poll/index.html', {
        'latest_questions': latest_questions,
    })

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, 'poll/details.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})
