from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Custom Admin Model
class AdminUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
