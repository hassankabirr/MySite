from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            name=instance.first_name,
            email=instance.email,
        )
def updateUser(sender, instance, created, **kwargs):
    user = instance.user
    if created == False:
        user.username = instance.username
        user.first_name = instance.name
        user.email = instance.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    print('heelp')
    if instance.user:
        print('heelp')
        instance.user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
