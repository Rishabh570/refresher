from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from vsitapp.models import Post
from .serializers import (
    PeopleSerializer,
    PeopleDetailSerializer,
)

class PeopleCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleDetailSerializer    

class PeopleView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleSerializer

class PeopleDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleDetailSerializer
    lookup_field = 'name'
