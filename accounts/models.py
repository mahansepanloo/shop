from django.db import models



class provider(models.Model):
    name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    provider = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class costomer(models.Model):
    name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    walet = models.IntegerField(default=100)

    def __str__(self):
        return self.name