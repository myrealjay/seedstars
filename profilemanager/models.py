from django.db import models

# Create your models here.

class profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100,unique= True)
    def __str__(self):
        return '{0} {1}'.format(self.name,self.email)
