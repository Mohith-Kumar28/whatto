from django.contrib import admin
from blog.models import Post
from blog.models import BlogComment

from embed_video.admin import AdminVideoMixin
# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register((Post,BlogComment))