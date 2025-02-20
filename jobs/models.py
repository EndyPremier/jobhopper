from django.db import models

# Create your models here.
class JobClass(models.Model):
    jobcode = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

class Socs(models.Model):
    detailedOccupation = models.IntegerField(unique=True)
    detailName = models.CharField(max_length=400)
    majorGroup = models.CharField(max_length=7)
    minorGroup = models.CharField(max_length=7)
    broadGroup = models.CharField(max_length=7)
    majorName = models.CharField(max_length=200)
    minorName = models.CharField(max_length=200)
    broadName = models.CharField(max_length=200)