# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


# Register your models here.


from .models import Location

admin.site.register(Location)
admin.site.register(Profile, UserAdmin)

