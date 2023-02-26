from django.contrib import admin
from .models import Post, TeamMember

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'informations', 'img_url','subteam')
    list_filter = ("subteam",)
    search_fields = ['subteam']

admin.site.register(Post, PostAdmin)
admin.site.register(TeamMember, )