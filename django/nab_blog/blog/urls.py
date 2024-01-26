from django.urls import path
from .views import post_list, blog_view, c_blog
urlpatterns =[
    path('', post_list, name='post_list'),
    path('post/<int:pk>', blog_view, name='blog_view'),
    path('c_post', c_blog, name='c_blog')
]