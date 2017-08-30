from django.db import models
from django.utils import timezone

# Create your models here.

class blogPost(models.Model):
	date = models.DateField(verbose_name=u'blog.date', default=timezone.now)
	image = models.ImageField(verbose_name=u'blog.image', blank=True, null=True)
	title = models.CharField(verbose_name=u'blog.title', max_length=50)
	description = models.TextField(verbose_name=u'blog.text')
	def __unicode__(self):
		return self.title
		