from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels={
            'first_name': "Name"
        }