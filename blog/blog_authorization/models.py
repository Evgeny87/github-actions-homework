from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
UserModel: User = get_user_model()


class UserProfile(models.Model):
    user: UserModel = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"


@receiver(post_save, sender=UserModel)
def user_saved_handler(instance: UserModel, created: bool, **kwargs):
    if not created:
        return

    UserProfile.objects.create(user=instance)
