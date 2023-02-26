from django.views import generic
from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'index.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'

class PostListIndex(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'