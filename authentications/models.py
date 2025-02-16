from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Custom Admin Model
class AdminUser(AbstractUser):
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.username
