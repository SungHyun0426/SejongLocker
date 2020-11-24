from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Locker(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    lockerId = models.CharField(max_length=3, default='A00', primary_key=True)
    availability = models.CharField(max_length=1, default='A')

    def is_available():
        if availability == 'A':
            return True
        return False
