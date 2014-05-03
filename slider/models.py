from django.db import models

# Create your models here.
class Slide(models.Model):
	header = models.CharField(max_length = 200)
	body = models.CharField(max_length = 500)
	#add image, link later later
	def __unicode__(self):
		to_return = ("header =" + self.header + " body = " + self.body)
		return(to_return)


class Contact(models.Model):
    """ Represents an instance of someone contacting us via the contact form """
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    

    date_added = models.DateField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return self.name