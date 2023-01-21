from django.db import models

# Create your models here.

class ML_Deploy(models.Model):
    SepalLengthCm = models.CharField(max_length=20)
    SepalWidthCm = models.CharField(max_length=20)
    PetalLengthCm = models.CharField(max_length=20)
    PetalWidthCm = models.CharField(max_length=20)

    def __str__(self):
        return self.e_name

    class Meta:
        db_table = "iris"