from django.db import models
from django.contrib.auth.models import User
import re


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

SUBTEAM = (
    (0,"Software"),
    (1,"Science"),
)

VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
]

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    informations = models.TextField()
    img_url = models.ImageField(upload_to='team_member_img/')
    subteam = models.IntegerField(choices=SUBTEAM)
    
    class Meta:
        ordering = ['subteam']

    def __str__(self):
        return self.name
    
    def subteam_str(self):
        return SUBTEAM[self.subteam][1]
