from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def _str_(self):
        return self.name
    




    