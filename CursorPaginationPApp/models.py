from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ename
    