from django.contrib import admin

# Register your models here.

from .models import BlogPost, another_blog_post,Student

admin.site.register(BlogPost)
admin.site.register(another_blog_post)
admin.site.register(Student)