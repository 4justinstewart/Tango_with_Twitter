from django.http import HttpResponse

def index(request):
  return HttpResponse("Twitter Deals say the world is about to be more awesome! <a href='/deals/about'>More about us</a>")

def about(request):
  return HttpResponse("Twitter Deals is an app that allows businesses to promote very temporary deals to active twitter users within a radius of their business. <a href='/deals/'>Back Home</a>")
