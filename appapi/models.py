from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class users(AbstractUser):
    phone=models.CharField(max_length=10,)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.username}"
    
    

    