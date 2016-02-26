from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    lasted_question_list = Question.objects.order_by('-pub_date')[:5] 
    output = ', '.join([q.question_text for q in lasted_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Ud se encuentra en la pregunta %s." % question_id)


def result(request, question_id):
	response = "Se encuentra en los resultados de la pregunta %s. "
	return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Ud esta votando en la pregunta %S" % question_id)