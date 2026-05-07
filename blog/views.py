from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def home(request):

    category = request.GET.get('category')
    search = request.GET.get('search')

    blogs = Blog.objects.all()

    if category:
        blogs = blogs.filter(category=category)

    if search:
        blogs = blogs.filter(title__icontains=search)

    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'home.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})