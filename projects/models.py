from django.db import models
import  uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

    def calcutVote(self):
        reviews = self.review_set.all()
        total_vote = reviews.count()
        up_vote = reviews.filter(value='up').count()
        vote_ratio = (up_vote*100/total_vote)
        self.vote_total = total_vote
        self.vote_ratio = vote_ratio
        self.save()
    @property
    def reviewers_list(self):
        return self.review_set.all().values_list('owner__id', flat=True)
    class Meta:
        ordering = ['-vote_ratio', '-vote_total']
class Review(models.Model):
    VALUE_CHOICES = (
        ('up', 'Up Vote'),
        ('down', 'Down vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=4, choices=VALUE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.value
    class Meta:
        unique_together = [['owner', 'project']]



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name