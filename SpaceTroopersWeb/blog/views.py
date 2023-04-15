from django.views import generic
from django.shortcuts import render
from .models import Post, TeamMember, AboutUs

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
        "team_member_mentors_list": TeamMember.objects.filter(subteam=2),
        "team_member_science_list": TeamMember.objects.filter(subteam=1),
        "team_member_software_list": TeamMember.objects.filter(subteam=0),
    }
    return render(request ,'team_member.html', queryset)

def aboutUs(request):
    queryset = {
        'about_us': AboutUs.objects.get(id = 1),
        'images': AboutUs.objects.get(id = 1).aboutusimage_set.all()
    }
    return render(request, 'about_us.html', queryset)