from django.db import models

# Create your models here.
class employess(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    age=models.IntegerField()

    def __str__(self):
        return self.name



