from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):
    user_1 = models.OneToOneField(
        User, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='user_1')
    user_2 = models.OneToOneField(
        User, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='user_2')

    def __str__(self):
        return self.user_2


class Message(models.Model):
    sender = models.CharField(max_length=128)
    text_message = models.CharField(
        max_length=255, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    dialog = models.ForeignKey(
        Dialog, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.sender
