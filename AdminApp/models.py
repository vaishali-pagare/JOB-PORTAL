from django.db import models
from datetime import datetime

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    work_status = models.CharField(max_length=10)
    resume = models.FileField(default='VaishaliResume.pdf')
    image = models.ImageField(default='abc.jpg', upload_to="Images")
    gender = models.CharField(max_length=10)
    DOB =  models.DateField(default = datetime.now)
    address = models.CharField(max_length=30)
    resume_headline = models.CharField(max_length=20)
    key_skills = models.CharField(max_length=40)
    class Meta:
        db_table = "UserInfo"

class UEmployment(models.Model):
    uname = models.ForeignKey(to='UserInfo',on_delete=models.CASCADE)
    cname = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    Join_date = models.DateField(default = datetime.now)
    salary = models.FloatField(default=0)
    profile =  models.CharField(max_length=30)
    notice_period = models.CharField(max_length=20)

    class Meta:
        db_table = "UEmployment"


class UserEducation(models.Model):
    uname = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    education =  models.CharField(max_length=25)
    university = models.CharField(max_length=25)
    course =  models.CharField(max_length=20)
    marks =  models.FloatField(default=35)
    year = models.IntegerField()
    class Meta:
        db_table = "UserEducation"


class Company(models.Model):
    cname = models.CharField(max_length=25)
    email = models.CharField(max_length=20,unique=True)
    phone = models.IntegerField()
    person =  models.CharField(max_length=25)
    type = models.ForeignKey(to='Industry', on_delete=models.CASCADE)
    pincode = models.IntegerField()
    address1 =  models.CharField(max_length=25)
    image1  = models.ImageField(default='abc.jpg', upload_to="Images")
    password =  models.CharField(max_length=25)
    plan = models.CharField(max_length=15)
    date = models.DateField(default = datetime.now)
    post = models.IntegerField(default=100)
    expiry_date = models.DateField(default= datetime.now)
    class Meta:
        db_table = "Company"


class Industry(models.Model):
    type = models.CharField(max_length=35)

    class Meta:
        db_table = "Industry"

    def __str__(self):
        return self.type


class Payment(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=20)
    balance = models.FloatField(default=1000)

    class Meta:
        db_table = "Payment"


class Job(models.Model):
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    Experience = models.CharField(max_length=20)
    salary = models.CharField(max_length=20,default= "Not Disclosed")
    start_date = models.DateField(default = datetime.now)
    skills = models.CharField(max_length=30)
    no_opening = models.IntegerField()
    Education = models.CharField(max_length=40)
    response = models.IntegerField(default=0)

    class Meta:
        db_table  = "Job"


class Apply(models.Model):
    uname = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    #company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    job = models.ForeignKey(to='Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=10,default="APPLY")
    date = models.DateField(default = datetime.now)
    class Meta:
        db_table  = "Apply"


class Msg(models.Model):
    uname = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    job = models.ForeignKey(to='Job', on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    date = models.DateField(default = datetime.now)
    msg = models.CharField(max_length=500)
    class Meta:
        db_table = "Msg"

