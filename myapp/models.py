from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,null=False,blank=False)
    email =models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    problem=models.TextField()
    date=models.DateField()

    def __str__(self):
       return self.name
class Lecturerinfo(models.Model):
        lecturer_id= models.AutoField
        lecturer_name=models.CharField(max_length=50) 
        lecturer_email=models.CharField(max_length=50) 
        lecturer_subject=models.CharField(max_length=50) 
class Course(models.Model):
    title = models.CharField(max_length=122)
    category =models.CharField(max_length=122)
    code=models.CharField(max_length=12)