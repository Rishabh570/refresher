from django.conf.urls import url
from django.contrib import admin

from .views import (
    PeopleView,
    PeopleDetailView,
    PeopleCreateView,
    PeopleDeleteView,
)

urlpatterns = [
    url(r'^people/$', PeopleView.as_view(), name='list'),
    url(r'^people/(?P<first_name>.*)/$', PeopleDetailView.as_view(), name='detail'),
    url(r'^people-delete/(?P<target>.*)/$', PeopleDeleteView.as_view(), name='delete'),
    url(r'^create/$', PeopleCreateView.as_view(), name='create'),
]