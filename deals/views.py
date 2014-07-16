from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
  context = RequestContext(request)
  context_dict = { 'passing_info': 'Is this Python interpolation into HTML?'}
  return render_to_response('deals/index.html', context_dict, context)

def about(request):
  return HttpResponse("Tweet and Treat is an app that allows businesses to promote very temporary deals to active twitter users within a radius of their business. <a href='/deals/'>Back Home</a>")
