from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.PostList.as_view(), name='post'),
    path('post-index', views.PostListIndex.as_view(), name='post_index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]