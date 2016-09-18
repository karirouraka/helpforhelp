# -*- coding: utf-8 -*-
from django import forms
from tutor_account.models import UserProfile, Help
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'speciality', 'term', 'subject', 'prefered_date_and_time',
                  'lesson_place', 'photo']

#
class UserRegistrationForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class HelpForm(forms.ModelForm):


    class Meta:
        model = Help
        fields = ['subject', 'definition']