from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.
class blogPostAdmin(SummernoteModelAdmin):
	...
admin.site.register(blogPost, blogPostAdmin)