from django.contrib.auth.models import User
from django.db import models


class CreationModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Message(CreationModel):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField(null=True, max_length=512)
    subject = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'message'
        ordering = ('created_date',)
