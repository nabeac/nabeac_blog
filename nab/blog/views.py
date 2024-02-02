from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, FormView
from .models import Post
from .forms import CPosts


class ListPost(ListView):
    queryset = Post.objects.all().order_by('-updat_date')
    context_object_name = 'list'
    template_name = 'blog/list.html'

    # def get_queryset(self):
    #     queryset = self.queryset.filter(title__contains='pyton').first()
    #     queryset.title = queryset.replace('python','***')
    #     queryset.save()
    #     return self.queryse

class PostView(DeleteView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'blog/post_view.html'



def createpost(request):
    blog_form = CPosts
    if request.method == 'GET':
        context = {'form': blog_form}
        return render(request=request, template_name='blog/create_post.html', context=context)
    else:

        title = request.POST.get('title')
        body = request.POST.get('body')
        creator = request.POST.get('creator')
        Post.objects.create(title=title, body=body, creator_id=creator)
        return redirect('ListPost')
