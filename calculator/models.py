from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    protein = models.FloatField(max_length=100)
    carbs = models.FloatField(max_length=100)
    fat = models.FloatField(max_length=100)
    kcal = models.IntegerField()

    def __str__(self):
        return self.name