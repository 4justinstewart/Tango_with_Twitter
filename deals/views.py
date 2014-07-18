from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from deals.models import Company, Deal
from deals.forms import CompanyForm, DealForm
from deals.twitter import *

def index(request):
  context = RequestContext(request)

  context_dict = { 'passing_info': 'Is this Python interpolation into HTML?', 'company_form': CompanyForm, 'deal_form': DealForm}
  
  return render_to_response('deals/index.html', context_dict, context)

def twitter(request):
    context = RequestContext(request)

    x = OAuth().request_oauthtoken(request)

    context_dict = { 'host' : x }

    return render_to_response('deals/twitter.html', context_dict, context)

def create_deal(request):
    context = RequestContext(request)

    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        deal_form = DealForm(request.POST)

        if company_form.is_valid() and deal_form.is_valid():
            comp = company_form.save(commit=True)
            deal = Deal(body=request.POST['body'], company_id=comp.pk)
            deal.save()

            return redirect('deals.views.twitter')
        else:
            print company_form.errors
            print deal_form.errors
    else:
        company_form = CompanyForm() # Need to investigate this further!
        deal_form = DealForm()
    # return render_to_response(request, 'deals/index.html', {'form': form})


