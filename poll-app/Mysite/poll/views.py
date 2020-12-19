from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.


def home(request):
    return render(request, "poll/home.html")


# Created the view for the /poll url
def index(request):
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "poll/index.html", context)


def detail_question(request, question_id):
    # Get an object, if it doesn't exist raise a 404 error
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/detail.html", {"question": question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # The ID of the selected choice, as a string
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "U didn't select a choice"
        }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.n_votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))


def test(request):
    message = "This is my message"
    return HttpResponse(message)
