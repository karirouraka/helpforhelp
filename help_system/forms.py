# -*- coding: utf-8 -*-
from django import forms
from help_system.models import UserProfile, Help, Reference, Record
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'speciality', 'term', 'subject', 'prefered_date_and_time',
                  'lesson_place', 'photo']


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['date', 'time']


class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = ['subject', 'definition']

class LogInForm(forms.Form):
    user_identification = forms.CharField(label='Email or Login', required=True)
    password = forms.CharField(label='Password', required=True)

class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ['text']


