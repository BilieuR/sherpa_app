# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# Create your models here.


class Location(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200, default='NULL')
    image = models.CharField(max_length=499, default='NULL')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

   
    def __str__(self):
        return self.title

class Users(models.Model):
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=16)
	familyName = models.CharField(max_length=20)
	firstName = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	phoneNumber = models.IntegerField()
	userType = models.CharField(max_length=4)
	created_at = models.DateTimeField(default=datetime.now, blank=True)


