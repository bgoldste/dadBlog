from django.db import models

# Create your models here.
class Slide(models.Model):
	header = models.CharField(max_length = 200)
	body = models.CharField(max_length = 500)
	#add image, link later later
	def __unicode__(self):
		to_return = ("header =" + self.header + " body = " + self.body)
		return(to_return)

