from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from slider.models import Slide
from django.views.generic import TemplateView
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact

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

def about(request):
	template = loader.get_template('slider/about.html')

	context = RequestContext(request, {})
	return HttpResponse(template.render(context))




class ContactView(CreateView):
    template_name = "contact/form.html"
    form_class = ContactForm
    model = Contact
    success_url = '/contact/thanks/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
       
        return super(ContactView, self).form_valid(form)