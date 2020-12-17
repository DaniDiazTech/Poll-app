from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
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
	return render(request, "poll/detail.html", {"question":question})


def result(request, question_id):
	return HttpResponse(f"This is the response of the question: {question_id}")


def vote(request, question_id):
	return HttpResponse(f"Upvote of question : {question_id}")


def test(request):
	message = "This is my message"
	return HttpResponse(message)
