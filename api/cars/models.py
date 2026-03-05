from django.db import models
class Car(models.Model):
    model = models.CharField(max_length=20)
    placas = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.model
