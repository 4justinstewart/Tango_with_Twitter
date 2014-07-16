from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from deals.models import Company, Deal
from deals.forms import CompanyForm, DealForm

def index(request):
  context = RequestContext(request)

  context_dict = { 'passing_info': 'Is this Python interpolation into HTML?', 'form': CompanyForm}
  
  return render_to_response('deals/index.html', context_dict, context)

def about(request):
  return HttpResponse("Tweet and Treat is an app that allows businesses to promote very temporary deals to active twitter users within a radius of their business. <a href='/deals/'>Back Home</a>")

def create_deal(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            
            return about(request)
        else:
            print form.errors
    else:
        form = CompanyForm()

    # return render_to_response(request, 'deals/index.html', {'form': form})


