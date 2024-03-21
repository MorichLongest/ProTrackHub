from django.shortcuts import render,redirect
from .models import BlogPost 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def courses(request):
    blog =blog.objects.all()
    return render(request, 'courses.html')

def login(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def notfound(request, exception):
    # Your custom 404 error handling logic goes here
    return render(request, '404.html', status=404)

@login_required(login_url='login')
def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')
def courses(request):
    return render(request, 'courses.html')

def login(request):
    return render(request, 'login.html')

def blog_post(request, blog_post_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog.html', context)



    