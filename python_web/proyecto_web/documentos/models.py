# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Documento(models.Model):
    edad = models.IntegerField(null=True, blank=True)
    fecha = models.DataTimeField(null=True, blank=True)

def __unicode__(self):
	return 'Documento - {0}'.format(self.id)
