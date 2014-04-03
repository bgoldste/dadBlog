from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from slider.models import Slide

# Create your views here.
def index(request):
	last_2_slides = Slide.objects.order_by('id')[:2]
	template = loader.get_template('slider/index.html')
	context = RequestContext(request, {
    	'last_2_slides':last_2_slides,
    	})
	return HttpResponse(template.render(context))

def contact(request):

	template = loader.get_template('slider/contact.html')

	context = RequestContext(request, {

		})
	return HttpResponse(template.render(context))