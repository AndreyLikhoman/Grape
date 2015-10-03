from django.shortcuts import render
from .models import Post, Category, Tags, Image, Video, Galery, Media
# Create your views here.

def categories_list():
	categories = Category.objects.filter(published = True, parent = None )
	return categories

def home_page(request):
	posts = Post.objects.filter(published = True).order_by('date')
	return render(request, 'blog/index.html', {'posts': posts, 'categories': categories_list()})

def post_detail(request, category, url):
    # post = get_object_or_404(Post, slug=url)
    categorySerch = Category.objects.filter(slug = category)
    post = Post.objects.filter(slug = url, category= categorySerch);
    images = Image.objects.filter(post = post[0])
    videos = Video.objects.filter(post = post[0])
    return render(request, 'blog/post.html', {'post': post[0], 'categories': categories_list(), 'images': images, 'videos': videos})

def category_detail(request, url):
    # post = get_object_or_404(Post, slug=url)
    category = Category.objects.filter(slug = url)
    sub_categories = Category.objects.filter(published = True, parent = category[0] )
    posts = Post.objects.filter(published = True, category = category[0] ).order_by('date')
    return render(request, 'blog/category.html', {'posts': posts, 'category': category[0], 'sub_categoties': sub_categories, 'categories': categories_list() })


def return_galeries(request):
    # post = get_object_or_404(Post, slug=url)
    galeries = Galery.objects.filter(parent = None);
    return render(request, 'blog/galery.html', {'galeries': galeries, 'categories': categories_list()})


def galery_detail(request, url):
    # post = get_object_or_404(Post, slug=url)
    galery = Galery.objects.filter(slug = url);
    images = Image.objects.filter(galery = galery[0])
    return render(request, 'blog/galerySlide.html', {'galery': galery[0], 'categories': categories_list(), 'images': images})

def return_medias(request):
    # post = get_object_or_404(Post, slug=url)
    medias = Media.objects.filter(parent = None);
    return render(request, 'blog/medias.html', {'medias': medias, 'categories': categories_list()})


def return_videos(request, url):
    # post = get_object_or_404(Post, slug=url)
    media = Media.objects.filter(slug = url);
    videos = Video.objects.filter(media = media[0])
    return render(request, 'blog/videos.html', {'media': media[0], 'categories': categories_list(), 'videos': videos})
