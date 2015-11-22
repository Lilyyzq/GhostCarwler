from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	
	#output = '<br />'.join([p.question_text for p in latest_question_list])
	return render(request,'polls/index.html',context)
	
def detail(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question':question})
	
def results(request,question_id):
	return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s." % question_id)