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

from vsitapp import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    # Admin Dashboard URL
    url(r'^admin/', admin.site.urls),

    # API URL
    url(r'^api/', include(("vsitapp.api.urls", "vsitapp"), namespace='vsitapp')),
    
    url('^$', views.home_login, name='home_login'),  # Ngrok uses this most of the times
    url(r'^home_login/$', views.home_login, name='home_login'),
    url(r'^help/$', views.help, name='help'),
    url(r'^list/$', views.list, name='list'),
    
    # Use this to delete all values stored in db
    url(r'^drop/$', views.drop),

    # User Credentials URLs
    url(r'^login/$', views.loginuser, name='login'),
    url(r'^logout/$', views.logoutuser, name='logout'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^passchangeform/$', views.passchange, name='passchangeform'),

    # Social Auth URLs
    url(r'^auth/', include('social_django.urls', namespace='social')),

    # AJAX URLs
    url(r'^upvote/$', views.upvote, name='upvote'),
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^list/$', views.list, name='upvoted_list'),
    url(r'^delete/$', views.delete_post, name='delete'),
    
]


# TODO: Host static files from S3 or somewhere
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
