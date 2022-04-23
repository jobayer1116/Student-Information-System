from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentDB(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=60)
    Semester = models.CharField(max_length=50)
    Roll = models.IntegerField(max_length=10,unique=True)
    Section = models.CharField(max_length=5)
    Gender = models.CharField(max_length=10)
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Contact = models.CharField(max_length=11,unique=True)
    Picture = models.ImageField(upload_to='media/upload/')

    class Meta:
        db_table = 'StudentDB'


class User_Info(models.Model):
    Id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='media/user/')

    class Meta:
        db_table = 'User_Info'


class Registration(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Class = models.IntegerField(max_length=10)
    Gender = models.CharField(max_length=10)
    Father_Name = models.CharField(max_length=50)
    Father_Nid = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Mother_Nid = models.CharField(max_length=50)
    Present_Address = models.TextField(max_length=250)
    Permanent_Address = models.TextField(max_length=250)
    Contact = models.CharField(max_length=11, unique=True)
    Student_Picture = models.ImageField(upload_to='media/Registration/')
    Email = models.EmailField(max_length=50)

    class Meta:
        db_table = 'Registration'


class Contact_Us(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=50)
    Description = models.TextField(max_length=600)

    class Meta:
        db_table = 'Contact_Us'

class Result(models.Model):
    Id = models.AutoField(primary_key=True)
    About = models.CharField(max_length=50)
    File = models.TextField(max_length=200)
    class Meta:
        db_table = 'Result'


class Notis(models.Model):
    Id = models.AutoField(primary_key=True)
    About = models.CharField(max_length=50)
    Discription = models.TextField(max_length=2000)

    class Meta:
        db_table = 'Notis'


class Event(models.Model):
    Id = models.AutoField(primary_key=True)
    About = models.CharField(max_length=500)
    Event_Pic = models.ImageField(upload_to='media/Event/')
    class Meta:
        db_table = 'Event'
