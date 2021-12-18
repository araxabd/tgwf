from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40)

    def __str__(self):
        return '{} : {}'.format(self.user, self.key)
