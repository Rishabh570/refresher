from rest_framework.serializers import ModelSerializer

from vsitapp.models import Post

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'name',
            'title',
        ]

class PeopleDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'name',
            'title',
            'story',
        ]
