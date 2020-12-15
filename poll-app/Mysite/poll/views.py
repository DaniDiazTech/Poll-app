# from django.shortcuts import render
from django.http import HttpResponse
from .models import Question # Create your views here.


# Created the view for the /poll url
def index(request):
	latest_question_list = Question.objects.order_by('-publish_date')[:5]
	# latest_questions = Question.objects.order_by("-pub_date")[:5]
	output = ", ".join(question.question_text for question in latest_question_list)

	# return HttpResponse("Awesome job,this is the index page" + "\n" + output
	return HttpResponse(output)


def detail_question(request, question_id):
	return HttpResponse(f"This is the detail view of the question: {question_id}")


def result(request, question_id):
	return HttpResponse(f"This is the response of the question: {question_id}")


def vote(request, question_id):
	return HttpResponse(f"Upvote of question : {question_id}")
