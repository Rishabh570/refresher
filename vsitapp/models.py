from vote.models import VoteModel
from django.db import models

# Create your models here.


class Post(VoteModel, models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    story = models.CharField(max_length=300)
    votings = models.IntegerField(blank=True, null=True, default=0)
    author = models.CharField(null=False, default='foo', max_length=30)

    class Meta:
        ordering = ('-votings',)

    def __str__(self):
        return self.name
