from django.conf.urls import patterns, url
from slider import views
from slider.views import ContactView

 #

 #url(r'^(?i)contact', views.contact, name='contact'),

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	

	url(r'^(?i)contact',  ContactView.as_view(), name='contact'),

   
	url(r'^(?i)about', views.about, name = 'about'),
	url(r'^(?i)Media-Golden-Rules', views.golden_rules, name = 'golden_rules'),
	url(r'^(?i)messaging-tips', views.about, name = 'messaging-tips'),
	url(r'^(?i)thanks', views.about, name = 'thanks'),
	)
