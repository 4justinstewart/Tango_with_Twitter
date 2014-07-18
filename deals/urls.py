from django.conf.urls import patterns, url
from deals import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'), 
    url(r'^twitter$', views.twitter, name='twitter'),
    url(r'^create_deal$', views.create_deal, name="create_deal")
)