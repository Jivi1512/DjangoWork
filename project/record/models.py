from django.db import models

class Record(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    City=models.CharField(max_length=20,null=True)
    Age=models.IntegerField(null=True)