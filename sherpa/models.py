# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Location(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200, default='NULL')
    rating = models.CharField(max_length=200, default='NULL')
    image = models.CharField(max_length=499, default='NULL')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

   
    def __str__(self):
        return self.title

class Profile(AbstractUser):
    phoneNumber = models.CharField(max_length=10)
    userType = models.CharField(max_length=4)
