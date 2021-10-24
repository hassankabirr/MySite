from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile, Skill, Message
class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': "Name"
        }
    def __init__(self, *args, **kwargs):
        super(UserCreation, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class UpdateProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'name', 'email', 'short_intro', 'bio', 'location', 'profile_img', 'social_github',
                   'social_twitter', 'social_linkedin', 'social_stackoverflow', 'social_website']


    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class SendMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'email', 'subject', 'body']
        labels = {
            'sender_name': 'Please enter your name:',
            'email': 'Email',
            'subject': 'Subject',
            'body': 'Message'
        }
    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
