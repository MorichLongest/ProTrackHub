"""
URL configuration for ProTrackHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from users.views import register, logout_view, login_view
from pages.views import (
    index,
    about,
    contact,
    courses,
    login,
    testimonial,
    team,
    notfound,
    blog,
    post,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name= 'home'),
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('courses/', courses, name= 'courses'),
    path('login/', login_view, name= 'login'),
    path('testimonial/', testimonial, name= 'testimonial'),
    path('team/', team, name= 'team'),
    path('notfound/', notfound, name= 'notfound'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('blog/', blog, name='blog'),
    path('post/', , name='post')
    Other URL patterns...


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.notfound'