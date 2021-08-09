from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile


def created_profile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


# @receiver(delete_user, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(created_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
