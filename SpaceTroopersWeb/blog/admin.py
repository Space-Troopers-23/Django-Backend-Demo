from django.contrib import admin
from .models import Post, TeamMember, AboutUs, AboutUsImage

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name','subteam', 'linkedin_url')
    list_filter = ("subteam",)
    search_fields = ['subteam']

class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 2

class AboutUsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title' ]}),
        ('Content',               {'fields': ['content']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title','pub_date')
    inlines = [AboutUsImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(AboutUs, AboutUsAdmin)