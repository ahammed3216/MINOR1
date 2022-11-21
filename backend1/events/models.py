from django.db import models
from django.contrib.auth import get_user_model
from django.conf import  settings

User=get_user_model()

class AdminModel(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name =models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField()

    def __str__(self):
        return self.username

