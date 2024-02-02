from django.shortcuts import render, redirect
from .models import User
from .forms import CUser


def createuser(request):
    blog_form = CUser
    if request.method == 'GET':
        context = {'form': blog_form}
        return render(request=request, template_name='blog/create_post.html', context=context)
    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        User.objects.create(username=username, password=password, phone=phone)
        return redirect('ListPost')

