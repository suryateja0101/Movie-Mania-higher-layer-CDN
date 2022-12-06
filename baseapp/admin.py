from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Organization)
admin.site.register(OrganizationPosts)

# admin.site.register(VideoPosts, VideoPostsAdmin)


@admin.register(VideoPosts)
class VideoPostsAdmin(admin.ModelAdmin):
    pass
