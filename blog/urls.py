"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import path
from posts.views import *

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', home, name='home'),
     path('post/<int:id>/', post_detail, name='post_detail'),
     path('create/', create_post, name='create_post'),
     path('update/<int:id>/', update_post, name='update_post'),

path('delete/<int:id>/', delete_post, name='delete_post'),
     path('api/', api_posts, name='api_posts'),
     path('api/', api_posts, name='api_posts'),

path('api/<int:id>/', api_post_detail, name='api_post_detail')
     
]
