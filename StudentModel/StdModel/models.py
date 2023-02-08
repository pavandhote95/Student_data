from django.db import models

class StudentModel(models.Model):
	rno=models.IntegerField()
	name=models.CharField(max_length=20)
	marks=models.IntegerField()
	#date=models.datetime.today()

# Create your models here.
