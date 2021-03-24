from django.db import models
 
class Oya(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    addr = models.CharField(max_length=1024)