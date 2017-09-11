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
		pass
	blog_posts = blogPost.objects.order_by('-date')
	blog_posts = blog_posts[:3]
	page = 0
	print(blog_posts)
	return render(request, 'Main/blog.html', {'blog_posts': blog_posts, 'page': page})

def blog_page(request, page):
	if request.method == 'POST':
		pass
	blog_posts = blogPost.objects.order_by('-date')
	page = int(page)
	blog_posts = blog_posts[page*3:page*3+3]
	for post in blog_posts:
		print(post.title)
	return render(request, 'Main/blog.html', {'blog_posts': blog_posts, 'page': page})	

def blog_create(request):
	if request.method == 'POST':
		form = blogPostForm(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save()
			return HttpResponseRedirect('/')
	form = blogPostForm()
	return render(request, 'Main/blog_create.html', {'form': form})

def blog_edit(request, post_id):
	post = blogPost.objects.get(id= post_id)
	if request.method == 'POST':
		pass
	form = blogPostForm(initial={'title': post.title, 'description': post.description})
	return render(request, 'Main/blog_edit.html', {'form': form})

def music(request):
	return render(request, 'Main/music.html')

def art(request):
	return render(request, 'Main/art.html')

def games(request):
	return render(request, 'Main/games.html')
