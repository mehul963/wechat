from django.db import models
from django.contrib.auth.models import User


class ChatText(models.Model):
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    text=models.CharField(max_length=1024)
    time=models.DateTimeField(auto_now=True)
