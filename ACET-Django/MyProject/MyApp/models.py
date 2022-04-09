from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=20)
	rollnum=models.CharField(max_length=30)
	age=models.IntegerField()
	mobile=models.IntegerField()
	email=models.EmailField(max_length=30)
	address=models.TextField(max_length=30)

	def __str__(self):
		return self.name+' '+self.email
