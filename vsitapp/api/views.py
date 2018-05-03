# IMPORTS ############################################

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,

)
from vsitapp.models import Post
from .serializers import (
    PeopleSerializer,
    PeopleDetailSerializer,
    PeopleCreateSerializer,

)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly

# #######################################################

class PeopleCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, first_name=self.request.user.first_name)  


class PeopleView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleSerializer


class PeopleDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleDetailSerializer
    lookup_field = 'first_name'


class PeopleDeleteView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PeopleDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'first_name'
    lookup_url_kwarg = 'target'

