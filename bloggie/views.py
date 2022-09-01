from audioop import reverse
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


from bloggie.forms import CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy


# Create your views here.

class ListOfPosts(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

class SinglePost(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    success_url = reverse_lazy('listofposts')
