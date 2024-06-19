from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .forms import PostForm, User_Register_Form
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog_form.html', {'form': form})

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_form.html', {'form': form})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog') 
    return render(request, 'blog_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = User_Register_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request, user)
            return redirect('blog')
    else:
        form = User_Register_Form()
          
    return render(request, 'registration/register.html', {'form': form})

def test(request):
    return HttpResponse('Test Page')

