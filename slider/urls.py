from django.conf.urls import patterns, url
from slider import views
from slider.views import ContactView



urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^(?i)contact', views.contact, name='contact'),

	url(r'^(?i)contact',  ContactView.as_view(), name='contact'),
    #url(r'thanks/$', TemplateView.as_view(template_name='contact/thanks.html'), name='contact_complete')
	url(r'^(?i)about', views.about, name = 'about'),
	url(r'^(?i)Media-Golden-Rules', views.about, name = 'golden_rules'),
	url(r'^(?i)messaging-tips', views.about, name = 'golden_rules'),
	)
