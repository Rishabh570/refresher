from django.conf.urls import url
from django.contrib import admin

from .views import (
    PeopleView,
    PeopleDetailView,
    PeopleCreateView,
)

urlpatterns = [
    url(r'^people/$', PeopleView.as_view(), name='list'),
    url(r'^(?P<name>.*)/$', PeopleDetailView.as_view(), name='detail'),
    url(r'^$', PeopleCreateView.as_view(), name='create'),
]