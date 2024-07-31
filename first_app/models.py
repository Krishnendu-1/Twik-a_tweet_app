from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Twik(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=150)
    photo=models.ImageField(upload_to='photos/', null=True, blank=True)# "Pillow" is used , a pythn imaging library
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'{self.user.username} - {self.text}'

