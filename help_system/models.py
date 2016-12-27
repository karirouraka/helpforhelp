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


    def save(self, *args, **kwargs):
        super(Subject, self).save(*args, **kwargs)
        subject = Subject.objects.get(pk=self.pk)
        if subject.pk % 2 == 0:
            help = Help.objects.first()
            help.definition += "method save() was executed for subject with pk = " + str(subject.pk)
            help.save()

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    registration_date = models.DateField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    speciality = models.ManyToManyField(Speciality, related_name='tutors')
    term = models.PositiveSmallIntegerField()
    subject = models.ManyToManyField(Subject, related_name='tutors')
    prefered_date_and_time = models.DateTimeField()
    lesson_place = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank='True', upload_to='images')
    registration_info = models.OneToOneField(User,related_name='profile',null=True)

    def __unicode__(self):
        return self.name + ' ' + self.surname

    def count_rendered_helps(self):
        return sum([help.received.count() for help in self.helps.all()])

class Reference(models.Model):
    author = models.ForeignKey(User, related_name="references")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(UserProfile, related_name='references')

class HelpTime(models.Model):
    time = models.TimeField()

    def __unicode__(self):
        return str(self.time)

    class Meta:
        ordering = ['time']

class HelpDate(models.Model):
    date = models.DateField()

    def __unicode__(self):
        return str(self.date)

class Record(models.Model):
    date = models.ForeignKey(HelpDate, related_name='record')
    time = models.ManyToManyField(HelpTime, related_name='record')
    help = models.ForeignKey('Help', related_name='records', null=True)


    class Meta:
        ordering = ['date']

    def __unicode__(self):
        record = str(self.date)
        for time in self.time.all():
            record  += ' ' + str(time)
        if self.help:
            return record + ' help_pk ' +  str(self.help.pk)
        return record


class Help(models.Model):
    tutor = models.ForeignKey(UserProfile, related_name='helps')
    subject = models.ForeignKey(Subject, related_name='helps', on_delete=models.SET_NULL, blank=True, null=True)
    definition = models.TextField(null=True)


    def __unicode__(self):
        return str(self.pk)

    def count_times_help_received(self):
        times_help_received = self.received.count()
        return times_help_received

class HelpReceived(models.Model):
    help = models.ForeignKey(Help, related_name='received')
    student = models.ForeignKey(UserProfile, related_name='received_helps')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.help.subject)
