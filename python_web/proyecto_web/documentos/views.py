# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Importar clase base para Vistas
# Las vistas manejan la logica del sitio web
from django.views.generic import View

# Metodod render retorna una respuesta
# Combina una plantilla con un diccionario de contexto
# Y retorna un objeto HttpResponse
from django.shortcuts import render

from documentos.models import Documento

# Create your views here..

# Crear vista de Documentos
# Definir metodo get
class Documentos(View):
	def get(self, request, *args, **kwargs):

		docs = Documento.objects.all()

		context = {
		    'docs': docs,
		    'encabezado': 'Mis documentos'
		}

		return render(
			request,
			'documento.html',
			context
		)