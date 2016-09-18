from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

class Speciality(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title



class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    registration_date = models.DateField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    speciality = models.ManyToManyField(Speciality, related_name='tutors')
    term = models.SmallIntegerField()
    subject = models.ManyToManyField(Subject, related_name='tutors')
    prefered_date_and_time = models.DateTimeField()
    lesson_place = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank='True', upload_to='images')
    registration_info = models.OneToOneField(User,related_name='profile',null=True)

    def __unicode__(self):
        return self.name + ' ' + self.surname



class Reference(models.Model):
    author = models.ForeignKey(User, related_name="references")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(UserProfile, related_name='references')




class Help(models.Model):
    tutor = models.ForeignKey(UserProfile, related_name='helps')
    date = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, related_name='helps', on_delete=models.SET_NULL, blank=True, null=True)
    definition = models.TextField(null=True)