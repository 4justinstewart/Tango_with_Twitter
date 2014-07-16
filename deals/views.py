from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from deals.models import Company, Deal
from deals.forms import CompanyForm, DealForm

def index(request):
  context = RequestContext(request)

  context_dict = { 'passing_info': 'Is this Python interpolation into HTML?', 'company_form': CompanyForm, 'deal_form': DealForm}
  
  return render_to_response('deals/index.html', context_dict, context)

def about(request):
  return HttpResponse("Tweet and Treat is an app that allows businesses to promote very temporary deals to active twitter users within a radius of their business. <a href='/deals/'>Back Home</a>")

def create_deal(request):
    context = RequestContext(request)

    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        deal_form = DealForm(request.POST)

        if company_form.is_valid() and deal_form.is_valid():
            comp = company_form.save(commit=True)
            deal = Deal(body=request.POST['body'], company_id=comp.pk)
            deal.save()

            return about(request)
        else:
            print company_form.errors
            print deal_form.errors
    else:
        company_form = CompanyForm()
        deal_form = DealForm()
    # return render_to_response(request, 'deals/index.html', {'form': form})


