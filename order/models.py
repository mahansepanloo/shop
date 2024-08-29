from django.db import models
from accounts.models import costomer
from Internet_package.models import internet

class Order(models.Model):
    user = models.ForeignKey(costomer, on_delete=models.CASCADE)
    pakage = models.ForeignKey(internet,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(null=True, blank=True)




    def __str__(self) -> str:
        return self.user.username