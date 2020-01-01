from django.db import models

# Create your models here.

class PetrolList(models.Model):
    Id = models.AutoField(primary_key=True)
    City = models.CharField(max_length=150)
    Price = models.CharField(max_length=50)
    Changes = models.CharField(max_length=50)
    FuelType=models.IntegerField(default=0)
    UpdatedOn=models.DateTimeField()

    def __str__(self):
        return self.City

