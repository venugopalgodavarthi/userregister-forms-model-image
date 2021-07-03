from django.db import models

# Create your models here.
class USERMODEL(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    phone=models.BigIntegerField()
    dob=models.DateField()
    cho=(("Male","MALE"),("Female","FEMALE"))
    gender=models.CharField(max_length=25,choices=cho)
    address=models.CharField(max_length=100)
    img=models.ImageField()