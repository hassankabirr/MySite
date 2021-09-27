from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

def createProfile(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            name=instance.first_name,
            email=instance.email,
        )
    else:
        instance.profile.username = instance.username
        instance.profile.name = instance.first_name
        instance.profile.email = instance.email
        instance.profile.save()


def deleteUser(sender, instance, **kwargs):
    print('heelp')
    if instance.user:
        print('heelp')
        instance.user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
