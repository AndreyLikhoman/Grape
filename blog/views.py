from django.shortcuts import render
from .models import Post, Category, Tags
# Create your views here.

def categories_list():
	categories = Category.objects.filter(published = True, parent = None )
	return categories

def home_page(request):
	posts = Post.objects.filter(published = True).order_by('date')
	return render(request, 'blog/index.html', {'posts': posts, 'categories': categories_list()})

def post_detail(request, url):
    # post = get_object_or_404(Post, slug=url)
    post = Post.objects.filter(slug = url)
    return render(request, 'blog/post.html', {'post': post[0], 'categories': categories_list()})

def category_detail(request, url):
    # post = get_object_or_404(Post, slug=url)
    category = Category.objects.filter(slug = url)
    sub_categories = Category.objects.filter(published = True, parent = category[0] )
    posts = Post.objects.filter(published = True, category = category[0] ).order_by('date')
    return render(request, 'blog/category.html', {'posts': posts, 'category': category[0], 'sub_categoties': sub_categories, 'categories': categories_list() })