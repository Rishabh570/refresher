from rest_framework.serializers import ModelSerializer

from vsitapp.models import Post

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'first_name',
            'title',
            'story',

        ]

class PeopleDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'first_name',
            'title',
            'story',
            'author',
            'votings',
        ]

class PeopleCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'story',
        ]

