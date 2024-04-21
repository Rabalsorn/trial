from django.db import models

# Create your models here.
class datachange(models.Model):
    name= models.CharField(max_length=20)
    desc= models.CharField(max_length=20)
    data= models.CharField(max_length=10, default=True)
    price = models.IntegerField(default=0)

