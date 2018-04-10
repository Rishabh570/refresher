"""vsit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from vsitapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API urls
    url(r'^api/list/', include(("vsitapp.api.urls", "vsitapp"), namespace='vsitapp')),
    url(r'^api-auth/', include('rest_framework.urls')),
    
    url('^home/$', views.home, name='home'),
    url('^$', views.home_login, name='home_login'),  # Ngrok uses this most of the times
    url(r'^home_login/$', views.home_login, name='home_login'),
    url(r'help/$', views.help, name='help'),
    url(r'^list/$', views.list, name='list'),
    
    # Use this to delete all values stored in db
    url(r'drop/$', views.drop),

    # Login/Logout urls
    url(r'^login/', views.loginuser, name='login'),
    url(r'^logout/', views.logoutuser, name='logout'),

    # Social auth urls
    url(r'^auth/', include('social_django.urls', namespace='social')),

    # Mail sending url
    url(r'^send_mail/$', views.sendemail, name='sendemail'),

    # AJAX urls
    url(r'list/views/upvote/$', views.upvote, name='upvote'),
    url(r'list/views/downvote/$', views.downvote, name='downvote'),
    url(r'list/views/list/$', views.list, name='upvoted_list'),
    url(r'list/views/delete/$', views.delete_post, name='delete'),
]

# TODO: Host static files from S3 or somewhere
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
