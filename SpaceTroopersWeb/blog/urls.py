from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.postList, name='post'),
    path('post-index', views.postListIndex, name='post_index'),
    path('posts/<int:id>', views.postDetail, name='post_detail'),

    path('team-member', views.teamMemberList, name='team-members'),
    path('team-members', views.teamMemberList, name='team-members'),

    path('about-us', views.aboutUs ,name = 'about_us')
]