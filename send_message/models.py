from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):
    user_1 = models.ForeignKey(
        User, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='user_1')
    user_2 = models.ForeignKey(
        User, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='user_2')

    def __str__(self):
        return self.user_2.username


class Message(models.Model):
    sender = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text_message = models.CharField(
        max_length=255, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    dialog = models.ForeignKey(
        Dialog, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.sender.username
