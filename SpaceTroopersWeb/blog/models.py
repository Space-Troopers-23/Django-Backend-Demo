from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

SUBTEAM = (
    (0,"Software"),
    (1,"Science"),
    (2,"Mentor"),
    (3,"Organization"),
)


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    informations = models.TextField()
    img = models.ImageField(upload_to='team_member_img/')
    subteam = models.IntegerField(choices=SUBTEAM)
    linkedin_url = models.CharField(max_length=250)
    class Meta:
        ordering = ['subteam']
    def __str__(self):
        return self.name
    
    def subteam_str(self):
        return SUBTEAM[self.subteam][1]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(TeamMember, on_delete= models.CASCADE,related_name='blog_posts',db_constraint=False)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    img = models.ImageField(upload_to='post_img/')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    class Meta:
        managed = True
        
    def __str__(self):
        return self.title

class AboutUsImage(models.Model):
    aboutUs = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    img = models.ImageField(upload_to='about_us/')
    class Meta:
        managed = True
    def __str__(self):
        return self.text