from django.db import models
from accounts.models import provider
class internet(models.Model):
    owner = models.ForeignKey(provider,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name