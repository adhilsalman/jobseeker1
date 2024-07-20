from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.Name
    
class job(models.Model):
    jobname= models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    qualification=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    poster=models.ImageField(upload_to="poster")
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.jobname
    
class student(models.Model):
    email=models.CharField(max_length=200)
    contact=models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    qualification=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    resume=models.FileField(upload_to="files",null=True)
    experience=models.CharField(max_length=20)
    options=(("male","male"),("female","female"))
    gender=models.CharField(max_length=20,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,related_name="profile")

    def __str__(self):
        return self.name

class applications(models.Model):
    jobs=models.ForeignKey(job,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("pending","pending"),("rejected","rejected"),("processing","processing"))
    status=models.CharField(max_length=30,choices=options,default="pending")