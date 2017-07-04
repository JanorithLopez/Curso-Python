# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Importar modelo 
from documentos.models import Documento

# Register your models here.
# Crear clase de admin.ModelAdmin

class DocumentoAdmin(admin.ModelAdmin):
	model = Documento
	list_display = ['nombre', 'fecha']

# Registrar ModelAdmin para cada modelo
admin.site.register(Documento, DocumentoAdmin)
