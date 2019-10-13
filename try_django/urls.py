"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import (
	blog_post_create_view,
    get_student
	)
from .views import *
from searches.views import search_view

urlpatterns = [
    path('', home_page),
    path('signup/', signup),
    path('login/', login_app),
    path('logout/', logout_app),
    path('blog-new/', blog_post_create_view),
    path('student/',get_student),
    path('blog/', include('blog.urls')),
    path('search/', search_view),
    re_path(r'^abouts?/$', about),
    path('contact/', contact_page),
    path('example/', example_page),
    path('example2/', example_page2),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # Test Mode (Not in Production)
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)