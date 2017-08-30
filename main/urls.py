from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	url(r'^$', views.main_page, name = 'main_page'),
	url(r'^about/$', TemplateView.as_view(template_name="main_page.html")),
	url(r'^blog/$', views.blog, name = 'blog'),
	url(r'^music/$', views.music, name = 'music'),
	url(r'^art/$', views.art, name = 'art'),
	url(r'^games/$', views.games, name = 'games'),
]