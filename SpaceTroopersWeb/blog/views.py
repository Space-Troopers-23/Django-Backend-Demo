from django.views import generic
from django.shortcuts import render
from .models import Post, TeamMember

def home(request):
    return render(request, 'index.html')

def postList(request):
    data = {
        "post_list": Post.objects.filter(status=1).order_by('-created_on')
    }
    return render(request, "post.html", data)

def postListIndex(request):
    queryset = {
        "post_list": Post.objects.filter(status=1).order_by('-created_on')
    }
    return render(request, "post_index.html", queryset)

def postDetail(request, id):
    data = {
        "post": Post.objects.get(id = id)
    }
    return render(request, "post_detail.html",data)

def teamMemberList(request):
    queryset = {
        "team_member_list": TeamMember.objects.all()
    }
    return render(request ,'team_member.html', queryset)