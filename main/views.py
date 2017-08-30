from django.shortcuts import render
#from .forms import *
from .models import *

# Create your views here.

def main_page(request):
	return render(request, 'Main/main_page.html')

def blog(request):
	if request.method == 'POST':
		print('lol')
	blog_posts = blogPost.objects.all()
	print(blog_posts)
	return render(request, 'Main/blog.html', {'blog_posts': blog_posts})

def music(request):
	return render(request, 'Main/music.html')

def art(request):
	return render(request, 'Main/art.html')

def games(request):
	return render(request, 'Main/games.html')
