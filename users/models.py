from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_img = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_stackoverflow = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)
class Skill(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    reciver = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='messages')
    is_read = models.BooleanField(default=False)
    sender_name = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self):
        return self.subject
