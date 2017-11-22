# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import models

# Create your models here.
class car(models.Model):
     make = models.CharField(max_length=140)
     Type = models.CharField(max_length=140)
     year = models.CharField(max_length=140)
     colour = models.CharField(max_length=140)
     price = models.DecimalField(max_digits=99999999,decimal_places=2)

     def __str__(self):
		       return str(self.make)
