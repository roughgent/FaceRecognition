# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    residence = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=150, null=True)
    semester = models.IntegerField(null=True)
    recorded_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Records"
