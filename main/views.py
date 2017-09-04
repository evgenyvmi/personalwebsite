from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import *
from .models import *
from .forms import *

# Create your views here.

def main_page(request):
	return render(request, 'Main/main_page.html')

def blog(request):
	if request.method == 'POST':
		print('lol')
	blog_posts = blogPost.objects.all()
	blog_posts = [blog_posts[0], blog_posts[1], blog_posts[2]]
	pages = 0
	print(blog_posts)
	return render(request, 'Main/blog.html', {'blog_posts': blog_posts, 'pages': pages})
def blog_create(request):
	if request.method == 'POST':
		form = blogPostForm(request.POST, request.FILES)
		if form.is_valid():
			print('hello')
			new_post = form.save()
			return HttpResponseRedirect('/')
	form = blogPostForm()
	return render(request, 'Main/blog_create.html', {'form': form})

def music(request):
	return render(request, 'Main/music.html')

def art(request):
	return render(request, 'Main/art.html')

def games(request):
	return render(request, 'Main/games.html')
