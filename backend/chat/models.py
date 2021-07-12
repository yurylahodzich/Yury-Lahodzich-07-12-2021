import os

from django.contrib.auth.models import User
from django.db import models


def get_upload_path(self, filename):
    return os.path.join(self.file_path(), filename)


class CreationModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Message(CreationModel):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField(null=True, max_length=512)
    subject = models.FileField(upload_to=get_upload_path, blank=True)

    def file_path(self):
        return os.path.join(f'subjects/{self.sender_id}-{self.receiver_id}/{self.id}')

    class Meta:
        db_table = 'message'
        ordering = ('created_date',)
