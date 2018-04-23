from django.contrib import admin
from apps.cuestionario.models import Respuesta, Pregunta

admin.site.register(Respuesta)
admin.site.register(Pregunta)