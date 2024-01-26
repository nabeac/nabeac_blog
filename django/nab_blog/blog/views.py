from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User


# from account.models import User


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/list.html', context)


def blog_view(request, pk):
    blog = Post.objects.get(pk=pk)
    return render(request, 'blog/blog.html', {'blog': blog})


def c_blog(request):
    if request.method == 'GET':
        user = User.objects.all()
        context = {'user': user}
        return render(request, 'blog/c_blog.html', context)
    else:
        title = request.POST.get('title')
        body = request.POST.get('body')
        nev = request.POST.get('nev')
        ca_blog = Post.objects.create(title=title, body=body, writer_id= nev)
        return redirect("post_list")
