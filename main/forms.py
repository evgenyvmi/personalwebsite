from .models import *
from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class blogPostForm(ModelForm):
	class Meta:
		model = blogPost
		fields = ('image', 'title','description')
		widgets = {
            'description': SummernoteWidget(),
            #'bar': SummernoteInplaceWidget(),
        }