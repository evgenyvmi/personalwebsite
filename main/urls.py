from django.conf.urls import url
from . import views
from .views import *
from django.views.generic import TemplateView, DeleteView


urlpatterns = [
	url(r'^$', views.main_page, name = 'main_page'),
	url(r'^about/$', TemplateView.as_view(template_name="main_page.html")),
	url(r'^blog/$', views.blog, name = 'blog'),
	url(r'^blog/create$', views.blog_create, name = 'blog_create'),
	url(r'^blog/page/([-1,0-9]{1,2})$', views.blog_page, name = 'blog_page'),
	url(r'^blog/edit/([-1,0-9]{1,2})$', views.blog_edit, name = 'blog_edit'),
	url(r'^blog/post/([-1,0-9]{1,2})$', views.post, name = 'post'),
	url(r'^blog/(?P<pk>\d+)/delete/$', BlogDeleteView.as_view(), name='blog_delete'),
	url(r'^music/$', views.music, name = 'music'),
	url(r'^music/create$', views.music, name = 'music_create'),
	url(r'^art/$', views.art, name = 'art'),
	url(r'^art/create$', views.art, name = 'art_create'),
	url(r'^games/$', views.games, name = 'games'),
]